
from pprint import pprint

from report_parser import parse_cbc_report


PDF_PATH = "sample_report.pdf"


try:

    report = parse_cbc_report(PDF_PATH)

    print("\n========== REPORT DATE ==========")
    print(report["report_date"])

    print("\n========== EXTRACTED CBC VALUES ==========")
    pprint(report["cbc_values"])

    print("\n========== MISSING PARAMETERS ==========")
    pprint(report["missing_parameters"])

    print("\n========== EXTRACTION SUMMARY ==========")

    total = len(report["cbc_values"])
    expected = 9

    print(f"Extracted: {total}/{expected}")

    if total == expected:
        print("All CBC parameters were extracted.")
    else:
        print("Some CBC parameters are missing.")

except Exception as error:

    print("\nPDF PARSING ERROR:")
    print(error)
