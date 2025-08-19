from give_bmi import give_bmi, apply_limit


def test_error_cases():
    """Test all error cases"""
    print("\nTesting error cases...\n")

    try:
        give_bmi("not a list", [1, 2])
        print("❌ Failed: Should reject non-list height")
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")

    try:
        give_bmi([1.7, 1.8], [65])
        print("❌ Failed: Should reject different sizes")
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")

    try:
        give_bmi([1.7, "string"], [65, 70])
        print("❌ Failed: Should reject non-numeric values")
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")

    try:
        give_bmi([1.7, -1.8], [65, 70])
        print("❌ Failed: Should reject negative height")
    except ValueError as e:
        print(f"✅ Correctly caught: {e}")


def main():
    """Test function for give_bmi and apply_limit."""
    try:
        height = [2.71, 1.15, 1.75, 1.92]
        weight = [165.3, 38.4, 62, 62]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

        test_error_cases()

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
