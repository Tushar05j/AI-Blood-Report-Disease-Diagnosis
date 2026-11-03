
from pathlib import Path
import math
import tempfile

import joblib
import pandas as pd
import markdown
import nh3

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from llm_service import generate_explanation
from report_parser import parse_cbc_report
from comparison import compare_reports as compare_cbc_reports


app = Flask(__name__)

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "random_forest_pipeline.joblib"

# Maximum combined upload size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


# --------------------------------------------------
# 1. MODEL CONFIGURATION
# --------------------------------------------------

FEATURES = [
    "WBC", "RBC", "HGB", "PLT", "NEUT",
    "LYMPH", "MONO", "EOS", "BASO"
]
# Default sample CBC values for quick testing
SAMPLE_VALUES = {
    "WBC": "3.7",
    "RBC": "4.9",
    "HGB": "15.6",
    "PLT": "275",
    "NEUT": "1.96",
    "LYMPH": "1.32",
    "MONO": "0.17",
    "EOS": "0.25",
    "BASO": "0.03"
}
DISEASE_MAP = {
    0: "Anemia",
    1: "Polycythemia",
    2: "Leukocytosis",
    3: "Leukopenia",
    4: "Thrombocytopenia",
    5: "Thrombocytosis",
    6: "Neutropenia",
    7: "Neutrophilia",
    8: "Lymphocytopenia",
    9: "Lymphocytosis",
    10: "Monocytes high",
    11: "Eosinophil high",
    12: "Basophil high",
    13: "Normal"
}


# --------------------------------------------------
# 2. LOAD RANDOM FOREST MODEL
# --------------------------------------------------

model = None
load_error = None

try:
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
    else:
        load_error = (
            "Model file missing. Copy random_forest_pipeline.joblib "
            "beside app.py."
        )

except Exception as exc:
    load_error = f"Unable to load model: {exc}"


# --------------------------------------------------
# 3. HOME / RANDOM FOREST PREDICTION
# --------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def index():

    values = SAMPLE_VALUES.copy()
    result = None
    error = load_error
    llm_error = None

    if request.method == "POST":

        values = {
            name: request.form.get(name, "").strip()
            for name in FEATURES
        }

        if model is None:
            error = load_error or "Model is unavailable."

        else:
            try:
                row = {}

                # Validate user input
                for name, raw in values.items():

                    if not raw:
                        raise ValueError(
                            f"Enter a value for {name}."
                        )

                    value = float(raw)

                    if not math.isfinite(value) or value < 0:
                        raise ValueError(
                            f"{name} must be a finite, "
                            "non-negative number."
                        )

                    row[name] = value

                # Prepare input for Random Forest
                x = pd.DataFrame([row], columns=FEATURES)

                # Random Forest prediction
                class_id = int(model.predict(x)[0])

                predicted_label = DISEASE_MAP.get(
                    class_id, f"Class {class_id}"
                )

                # Model vote estimates
                votes = []

                if hasattr(model, "predict_proba"):

                    probs = model.predict_proba(x)[0]

                    clf = (
                        model.named_steps["model"]
                        if hasattr(model, "named_steps")
                        else model
                    )

                    votes = sorted(
                        [
                            {
                                "label": DISEASE_MAP.get(
                                    int(c), f"Class {c}"
                                ),
                                "percent": round(
                                    float(p) * 100, 1
                                )
                            }
                            for c, p in zip(clf.classes_, probs)
                        ],
                        key=lambda item: item["percent"],
                        reverse=True
                    )

                # Random Forest result
                result = {
                    "id": class_id,
                    "label": predicted_label,
                    "votes": votes,
                    "ai_explanation": None
                }

                # Groq LLM explanation
                try:

                    raw_explanation = generate_explanation(
                        prediction=predicted_label,
                        cbc_values=row
                    )

                    formatted_html = markdown.markdown(
                        raw_explanation,
                        extensions=["tables", "nl2br"]
                    )

                    result["ai_explanation"] = nh3.clean(
                        formatted_html,
                        tags={
                            "h2", "h3", "h4",
                            "p", "strong", "em",
                            "ul", "ol", "li",
                            "table", "thead", "tbody",
                            "tr", "th", "td",
                            "br", "blockquote", "code"
                        }
                    )

                except Exception:

                    app.logger.exception(
                        "Groq explanation generation failed"
                    )

                    llm_error = (
                        "AI explanation is temporarily unavailable. "
                        "Your Random Forest prediction was generated "
                        "successfully."
                    )

                error = None

            except (ValueError, TypeError) as exc:
                error = str(exc)

            except Exception as exc:
                app.logger.exception("Prediction failed")
                error = f"Prediction failed: {exc}"

    return render_template(
        "index.html",
        features=FEATURES,
        values=values,
        result=result,
        error=error,
        llm_error=llm_error
    )


# --------------------------------------------------
# 4. CBC REPORT COMPARISON
# --------------------------------------------------

@app.route("/compare-reports", methods=["GET", "POST"])
def compare_reports():

    error = None
    previous_report = None
    latest_report = None
    comparison = None

    if request.method == "POST":

        previous_file = request.files.get("previous_report")
        latest_file = request.files.get("latest_report")

        # Check that both files were selected
        if (
            previous_file is None
            or latest_file is None
            or not previous_file.filename
            or not latest_file.filename
        ):
            error = (
                "Please upload both previous and latest CBC reports."
            )

        else:

            previous_name = secure_filename(
                previous_file.filename
            )

            latest_name = secure_filename(
                latest_file.filename
            )

            # Validate file extensions
            if (
                Path(previous_name).suffix.lower() != ".pdf"
                or Path(latest_name).suffix.lower() != ".pdf"
            ):
                error = "Only PDF files are supported."

            else:
                try:

                    # Temporary directory is automatically deleted
                    # after both reports have been processed.
                    with tempfile.TemporaryDirectory() as temp_dir:

                        previous_path = (
                            Path(temp_dir) / "previous_report.pdf"
                        )

                        latest_path = (
                            Path(temp_dir) / "latest_report.pdf"
                        )

                        # Save uploaded PDFs temporarily
                        previous_file.save(previous_path)
                        latest_file.save(latest_path)

                        # Extract CBC values
                        previous_report = parse_cbc_report(
                            previous_path
                        )

                        latest_report = parse_cbc_report(
                            latest_path
                        )

                        # Validate extracted data
                        if not previous_report["cbc_values"]:
                            raise ValueError(
                                "No CBC parameters could be extracted "
                                "from the previous report."
                            )

                        if not latest_report["cbc_values"]:
                            raise ValueError(
                                "No CBC parameters could be extracted "
                                "from the latest report."
                            )

                        # Compare both reports
                        comparison = compare_cbc_reports(
                            previous_report,
                            latest_report
                        )

                    # Temporary files are deleted here.

                except (ValueError, FileNotFoundError) as exc:

                    error = str(exc)

                    previous_report = None
                    latest_report = None
                    comparison = None

                except Exception:

                    app.logger.exception(
                        "CBC report processing failed"
                    )

                    error = (
                        "Unable to process the uploaded reports. "
                        "Please check that both PDFs are valid, "
                        "text-readable CBC reports."
                    )

                    previous_report = None
                    latest_report = None
                    comparison = None

    return render_template(
        "compare_reports.html",
        error=error,
        previous_report=previous_report,
        latest_report=latest_report,
        comparison=comparison
    )


# --------------------------------------------------
# 5. FILE SIZE ERROR HANDLER
# --------------------------------------------------

@app.errorhandler(413)
def file_too_large(exc):

    return render_template(
        "compare_reports.html",
        error=(
            "The uploaded files exceed the 10 MB combined limit."
        ),
        previous_report=None,
        latest_report=None,
        comparison=None
    ), 413


# --------------------------------------------------
# 6. RUN FLASK APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
