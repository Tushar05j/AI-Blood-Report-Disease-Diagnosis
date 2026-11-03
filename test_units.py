
from comparison import normalize_unit


test_cases = [
    ("10^3/uL", "10³/µL"),
    ("10^6/uL", "10⁶/μL"),
    ("g/dL", "G/DL"),
    ("10^3 / uL", "10³/μL")
]

print("\n========== UNIT NORMALIZATION TEST ==========")

for unit1, unit2 in test_cases:

    normalized1 = normalize_unit(unit1)
    normalized2 = normalize_unit(unit2)

    passed = normalized1 == normalized2

    print(f"\nUnit 1: {unit1}")
    print(f"Unit 2: {unit2}")
    print(f"Normalized 1: {normalized1}")
    print(f"Normalized 2: {normalized2}")
    print("Result:", "PASS" if passed else "FAIL")
