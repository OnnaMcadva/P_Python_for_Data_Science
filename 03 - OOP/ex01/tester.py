from S1E7 import Baratheon, Lannister


def check(title, value, expected=None):
    """Utility function for structured checks with safe output."""
    try:
        print(f"{title}: {value}")
        if expected is not None:
            print(f"   -> Expected: {expected}")
            if value != expected:
                print(f"❌ Failed: {title}")
            else:
                print(f"✅ Passed: {title}")
    except Exception as e:
        print(f"⚠️ Exception in test '{title}': {e}")


def test_baratheon():
    print("=== Testing Baratheon ===\n")
    try:
        Robert = Baratheon("Robert")
        check("Robert __dict__", Robert.__dict__)
        check("Robert __str__", Robert.__str__)
        check("Robert __repr__", Robert.__repr__)
        check("Robert.is_alive (before die)", Robert.is_alive, True)

        Robert.die()
        check("Robert.is_alive (after die)", Robert.is_alive, False)
        check("Robert.__doc__", Robert.__doc__, "Represent Baratheon family.")
    except Exception as e:
        print(f"⚠️ Exception in Baratheon tests: {e}")
    print("---")


def test_lannister():
    print("=== Testing Lannister ===\n")
    try:
        Cersei = Lannister("Cersei")
        check("Cersei __dict__", Cersei.__dict__)
        check("Cersei __str__", Cersei.__str__)
        check("Cersei.is_alive", Cersei.is_alive, True)
    except Exception as e:
        print(f"⚠️ Exception in Lannister tests: {e}")
    print("---")


def test_lannister_factory():
    print("=== Testing Lannister factory method ===\n")
    try:
        Jaine = Lannister.create_lannister("Jaine", True)
        check("Jaine name + family", (
            Jaine.first_name, Jaine.family_name), ("Jaine", "Lannister"))
        check("Jaine.is_alive", Jaine.is_alive, True)
        print(
            f"Formatted: Name : ({Jaine.first_name}, "
            f"{type(Jaine).__name__}), "
            f"Alive : {Jaine.is_alive}")
    except Exception as e:
        print(f"⚠️ Exception in Lannister factory tests: {e}")


def main():
    test_baratheon()
    test_lannister()
    test_lannister_factory()
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    main()
