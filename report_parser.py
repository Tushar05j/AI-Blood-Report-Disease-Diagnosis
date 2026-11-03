
import re
import pymupdf

from pathlib import Path


# --------------------------------------------------
# 1. CBC PARAMETERS AND ALIASES
# --------------------------------------------------

CBC_ALIASES = {
    "WBC": [
        "WBC",
        "White Blood Cell Count",
        "Total Leukocyte Count",
        "Total Leucocyte Count",
        "TLC"
    ],
    "RBC": [
        "RBC",
        "Red Blood Cell Count",
        "Red Cell Count",
        "Erythrocyte Count"
    ],
    "HGB": [
        "HGB",
        "HB",
        "Hemoglobin",
        "Haemoglobin"
    ],
    "PLT": [
        "PLT",
        "Platelet Count",
        "Platelets",
        "Thrombocyte Count"
    ],
    "NEUT": [
        "NEUT",
        "Neutrophils",
        "Neutrophil Count",
        "Absolute Neutrophil Count",
        "ANC"
    ],
    "LYMPH": [
        "LYMPH",
        "Lymphocytes",
        "Lymphocyte Count",
        "Absolute Lymphocyte Count",
        "ALC"
    ],
    "MONO": [
        "MONO",
        "Monocytes",
        "Monocyte Count"
    ],
    "EOS": [
        "EOS",
        "Eosinophils",
        "Eosinophil Count"
    ],
    "BASO": [
        "BASO",
        "Basophils",
        "Basophil Count"
    ]
}


# --------------------------------------------------
# 2. HELPER FUNCTIONS
# --------------------------------------------------

NUMBER = r"[-+]?\d+(?:,\d{3})*(?:\.\d+)?"

RANGE_PATTERN = re.compile(
    rf"^\s*({NUMBER})\s*(?:-|–|to)\s*({NUMBER})\s*$",
    re.IGNORECASE
)


def normalize_label(label):
    return re.sub(r"[^a-z0-9]", "", label.lower())


def extract_number(value):
    try:
        return float(value.replace(",", "").strip())
    except (ValueError, AttributeError):
        return None



def identify_parameter(line):
    """
    Identify CBC parameters even when the report
    includes abbreviations in parentheses.

    Examples:
    Hemoglobin (HGB) -> HGB
    Platelet Count (PLT) -> PLT
    Neutrophils (NEUT) -> NEUT
    """

    normalized = normalize_label(line)

    for parameter, aliases in CBC_ALIASES.items():

        for alias in aliases:

            alias_normalized = normalize_label(alias)

            # Exact label match
            if normalized == alias_normalized:
                return parameter, alias

            # Label followed by its parameter abbreviation
            if normalized == alias_normalized + parameter.lower():
                return parameter, alias

    return None, None


# --------------------------------------------------
# 3. PDF TEXT EXTRACTION
# --------------------------------------------------

def extract_pdf_text(pdf_path):

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Please upload a PDF file.")

    with pymupdf.open(pdf_path) as document:

        if document.is_encrypted:
            raise ValueError("Password-protected PDFs are not supported.")

        if len(document) == 0:
            raise ValueError("The uploaded PDF is empty.")

        pages = [page.get_text("text") for page in document]

    text = "\n".join(pages).strip()

    if not text:
        raise ValueError(
            "No readable text found. The PDF may be scanned."
        )

    return text


# --------------------------------------------------
# 4. EXTRACT CBC VALUES
# --------------------------------------------------

def extract_cbc_values(text):

    results = {}

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for index, line in enumerate(lines):

        parameter, alias = identify_parameter(line)

        if parameter is None or parameter in results:
            continue

        # Search a small window after the parameter label.
        # Stop if another CBC parameter begins.
        candidate_lines = []

        for next_line in lines[index + 1:index + 6]:

            next_parameter, _ = identify_parameter(next_line)

            if next_parameter is not None:
                break

            candidate_lines.append(next_line)

        # Find the first valid numeric result.
        value = None
        value_position = None

        for position, candidate in enumerate(candidate_lines):

            if re.fullmatch(NUMBER, candidate):
                value = extract_number(candidate)
                value_position = position
                break

        if value is None:
            continue

        # Look for unit and reference range after the value.
        remaining_lines = candidate_lines[value_position + 1:]

        unit = None
        reference_range = None

        for candidate in remaining_lines:

            # Match reference range.
            range_match = RANGE_PATTERN.fullmatch(candidate)

            if range_match:
                low = extract_number(range_match.group(1))
                high = extract_number(range_match.group(2))

                if low is not None and high is not None and low <= high:
                    reference_range = {
                        "low": low,
                        "high": high
                    }

                continue

            # Capture likely measurement units.
            if unit is None and re.search(
                r"(?:10\s*\^?\s*[36]|/|%|g|mg|pg|fL|uL|µL|μL)",
                candidate,
                re.IGNORECASE
            ):
                unit = candidate

        results[parameter] = {
            "value": value,
            "unit": unit,
            "reference_range": reference_range,
            "source_label": alias,
            "verified": False
        }

    return results


# --------------------------------------------------
# 5. EXTRACT REPORT DATE
# --------------------------------------------------

def extract_report_date(text):

    date_patterns = [
        r"\b\d{1,2}\s+[A-Za-z]+\s+\d{4}\b",
        r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b",
        r"\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b"
    ]

    for pattern in date_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(0)

    return None


# --------------------------------------------------
# 6. MAIN REPORT PARSER
# --------------------------------------------------

def parse_cbc_report(pdf_path):

    text = extract_pdf_text(pdf_path)

    cbc_values = extract_cbc_values(text)

    report_date = extract_report_date(text)

    missing_parameters = [
        parameter
        for parameter in CBC_ALIASES
        if parameter not in cbc_values
    ]

    return {
        "report_date": report_date,
        "cbc_values": cbc_values,
        "missing_parameters": missing_parameters,
        "extracted_text": text
    }
