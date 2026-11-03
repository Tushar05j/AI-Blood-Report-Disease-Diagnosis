
# comparison.py

import re
import unicodedata


# --------------------------------------------------
# 1. CBC PARAMETERS
# --------------------------------------------------

CBC_PARAMETERS = [
    "WBC",
    "RBC",
    "HGB",
    "PLT",
    "NEUT",
    "LYMPH",
    "MONO",
    "EOS",
    "BASO"
]


# --------------------------------------------------
# 2. UNIT NORMALIZATION
# --------------------------------------------------

import re

def normalize_unit(unit):
    if not unit:
        return None

    unit = str(unit).strip().lower()

    # Convert Unicode superscript digits
    superscripts = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    unit = unit.translate(superscripts)

    # Restore exponent notation: 103 -> 10^3, 106 -> 10^6
    unit = re.sub(r"10([36])", r"10^\1", unit)

    # Normalize micro symbols
    unit = unit.replace("μ", "u").replace("µ", "u")

    # Remove spaces
    unit = re.sub(r"\s+", "", unit)

    return unit


# --------------------------------------------------
# 3. REFERENCE RANGE COMPARISON
# --------------------------------------------------

def compare_reference_range(value, reference_range):
    """
    Compare a value against the laboratory reference range.
    """

    if not reference_range:
        return "Not available"

    low = reference_range.get("low")
    high = reference_range.get("high")

    if low is None or high is None:
        return "Not available"

    if value < low:
        return "Below range"

    if value > high:
        return "Above range"

    return "Within range"


# --------------------------------------------------
# 4. CALCULATE CHANGES
# --------------------------------------------------

def calculate_change(previous_value, latest_value):
    """
    Calculate absolute and percentage changes.
    """

    absolute_change = latest_value - previous_value

    if previous_value == 0:
        percentage_change = None
    else:
        percentage_change = (
            absolute_change / abs(previous_value)
        ) * 100

    if absolute_change > 0:
        direction = "Increased"
    elif absolute_change < 0:
        direction = "Decreased"
    else:
        direction = "Unchanged"

    return {
        "absolute_change": round(absolute_change, 3),

        "percentage_change": (
            round(percentage_change, 2)
            if percentage_change is not None
            else None
        ),

        "direction": direction
    }


# --------------------------------------------------
# 5. COMPARE TWO CBC REPORTS
# --------------------------------------------------

def compare_reports(previous_report, latest_report):
    """
    Compare two parsed CBC reports.

    Inputs:
        previous_report: Output of parse_cbc_report()
        latest_report: Output of parse_cbc_report()

    Returns:
        Structured comparison results.
    """

    previous_values = previous_report.get("cbc_values", {})
    latest_values = latest_report.get("cbc_values", {})

    comparison_results = []

    for parameter in CBC_PARAMETERS:

        previous = previous_values.get(parameter)
        latest = latest_values.get(parameter)

        # Check parameter availability.
        if previous is None or latest is None:

            comparison_results.append({
                "parameter": parameter,
                "status": "Missing",
                "message": "Parameter not found in both reports."
            })

            continue

        previous_value = previous.get("value")
        latest_value = latest.get("value")

        previous_unit = previous.get("unit")
        latest_unit = latest.get("unit")

        # Validate extracted values.
        if previous_value is None or latest_value is None:

            comparison_results.append({
                "parameter": parameter,
                "status": "Invalid",
                "message": "One or both values are invalid."
            })

            continue

        # Check unit availability.
        if not previous_unit or not latest_unit:

            comparison_results.append({
                "parameter": parameter,
                "status": "Unit missing",
                "message": "Unit information is unavailable."
            })

            continue

        # Normalize units before comparison.
        normalized_previous_unit = normalize_unit(previous_unit)
        normalized_latest_unit = normalize_unit(latest_unit)

        # Reject incompatible units.
        if normalized_previous_unit != normalized_latest_unit:

            comparison_results.append({
                "parameter": parameter,
                "status": "Unit mismatch",
                "previous_unit": previous_unit,
                "latest_unit": latest_unit,
                "message": "Units differ. Convert or verify before comparison."
            })

            continue

        # Calculate numerical changes.
        change = calculate_change(
            previous_value,
            latest_value
        )

        # Compare against each report's own reference range.
        previous_range_status = compare_reference_range(
            previous_value,
            previous.get("reference_range")
        )

        latest_range_status = compare_reference_range(
            latest_value,
            latest.get("reference_range")
        )

        # Store comparison result.
        comparison_results.append({

            "parameter": parameter,

            "previous_value": previous_value,
            "latest_value": latest_value,

            "unit": previous_unit,

            "absolute_change": change["absolute_change"],
            "percentage_change": change["percentage_change"],
            "direction": change["direction"],

            "previous_reference_status": previous_range_status,
            "latest_reference_status": latest_range_status,

            "previous_reference_range": previous.get("reference_range"),
            "latest_reference_range": latest.get("reference_range"),

            "status": "Compared"
        })

    return {
        "previous_report_date": previous_report.get("report_date"),
        "latest_report_date": latest_report.get("report_date"),
        "results": comparison_results
    }
