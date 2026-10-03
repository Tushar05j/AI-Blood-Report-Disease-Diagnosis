from pathlib import Path
import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "random_forest_pipeline.joblib"
FEATURES = ["WBC", "RBC", "HGB", "PLT", "NEUT", "LYMPH", "MONO", "EOS", "BASO"]

# Confirm IDs against the dataset documentation before presenting.
DISEASE_MAP = {
    0:"Anemia", 1:"Polycythemia", 2:"Leukocytosis", 3:"Leukopenia",
    4:"Thrombocytopenia", 5:"Thrombocytosis", 6:"Neutropenia",
    7:"Neutrophilia", 8:"Lymphocytopenia", 9:"Lymphocytosis",
    10:"Monocytes high", 11:"Eosinophil high", 12:"Basophil high", 13:"Normal"
}
model = None
load_error = None
try:
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
    else:
        load_error = "Model file missing. Copy random_forest_pipeline.joblib beside app.py."
except Exception as exc:
    load_error = f"Unable to load model: {exc}"

@app.route("/", methods=["GET", "POST"])
def index():
    values = {name:"" for name in FEATURES}
    result, error = None, load_error
    if request.method == "POST":
        values = {name:request.form.get(name,"").strip() for name in FEATURES}
        if model is None:
            error = load_error or "Model is unavailable."
        else:
            try:
                row = {}
                for name, raw in values.items():
                    if not raw:
                        raise ValueError(f"Enter a value for {name}.")
                    value = float(raw)
                    if pd.isna(value) or value < 0:
                        raise ValueError(f"{name} must be a non-negative number.")
                    row[name] = value
                # Keep feature names and order identical to training.
                x = pd.DataFrame([row], columns=FEATURES)
                class_id = int(model.predict(x)[0])
                votes = []
                if hasattr(model, "predict_proba"):
                    probs = model.predict_proba(x)[0]
                    clf = model.named_steps["model"] if hasattr(model, "named_steps") else model
                    votes = sorted([
                        {"label":DISEASE_MAP.get(int(c),f"Class {c}"),
                         "percent":round(float(p)*100,1)}
                        for c,p in zip(clf.classes_,probs)
                    ], key=lambda item:item["percent"], reverse=True)
                result = {"id":class_id,
                          "label":DISEASE_MAP.get(class_id,f"Class {class_id}"),
                          "votes":votes}
                error = None
            except (ValueError, TypeError) as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Prediction failed: {exc}"
    return render_template("index.html", features=FEATURES, values=values,
                           result=result, error=error)

if __name__ == "__main__":
    # Local classroom demo only; debug mode is not for public deployment.
    app.run(debug=True)
