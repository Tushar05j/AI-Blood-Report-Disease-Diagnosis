
# test_comparison.py

from pprint import pprint

from report_parser import parse_cbc_report
from comparison import compare_reports


# --------------------------------------------------
# 1. LOAD PREVIOUS REPORT
# --------------------------------------------------

previous_report = parse_cbc_report("sample_report.pdf")


# --------------------------------------------------
# 2. CREATE A SIMULATED LATEST REPORT
# --------------------------------------------------

latest_report = {
    "report_date": "02 November 2026",
    "cbc_values": {}
}

# Simulated values for testing only.
latest_values = {
    "WBC": 4.50,
    "RBC": 4.80,
    "HGB": 15.20,
    "PLT": 290.0,
    "NEUT": 2.20,
    "LYMPH": 1.50,
    "MONO": 0.25,
    "EOS": 0.30,
    "BASO": 0.04
}

# Reuse the previous report's units and reference ranges.
for parameter, data in previous_report["cbc_values"].items():

    latest_report["cbc_values"][parameter] = {
        "value": latest_values[parameter],
        "unit": data["unit"],
        "reference_range": data["reference_range"],
        "source_label": data["source_label"],
        "verified": True
    }


# --------------------------------------------------
# 3. COMPARE BOTH REPORTS
# --------------------------------------------------

comparison = compare_reports(
    previous_report,
    latest_report
)


# --------------------------------------------------
# 4. DISPLAY RESULTS
# --------------------------------------------------

print("\n========== REPORT COMPARISON ==========")

print("Previous report:", comparison["previous_report_date"])
print("Latest report:", comparison["latest_report_date"])

print("\n========== CBC COMPARISON RESULTS ==========")

for item in comparison["results"]:

    print("\nParameter:", item["parameter"])
    print("Status:", item["status"])

    if item["status"] == "Compared":

        print("Previous:", item["previous_value"])
        print("Latest:", item["latest_value"])
        print("Change:", item["absolute_change"])
        print("Percentage change:", item["percentage_change"])
        print("Direction:", item["direction"])

        print(
            "Previous reference status:",
            item["previous_reference_status"]
        )

        print(
            "Latest reference status:",
            item["latest_reference_status"]
        )

    else:
        print("Message:", item.get("message"))
