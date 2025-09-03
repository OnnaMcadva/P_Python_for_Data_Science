from S1E9 import Character, Stark


def main():
    try:
        print("=== Test 1: Ned Stark ===")
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print("Alive?", Ned.is_alive)
        Ned.die()
        print("Alive after die():", Ned.is_alive)
        print("Class docstring:", Ned.__doc__)
        print("Init docstring:", Ned.__init__.__doc__)
        print("Die docstring:", Ned.die.__doc__)

        print("\n=== Test 2: Lyanna Stark (already dead) ===")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        Lyanna.die()
        print("Alive after die():", Lyanna.is_alive)

        print("\n=== Test 3: Abstract class instantiation ===")
        try:
            hodor = Character("Hodor")
            print("ERROR: Character should not be instantiable!", hodor)
        except TypeError as e:
            print("Caught expected error:", e)

        print("\n=== Test 4: Input validation ===")
        bad = None
        try:
            bad = Stark(123)  # not a string
        except Exception as e:
            print("Caught expected error:", e)
        print("Value of bad after exception:", bad)

        very_bad = None
        try:
            very_bad = Stark("Bran", "yes")  # not a bool
        except Exception as e:
            print("Caught expected error:", e)
        print("Value of very_bad after exception:", very_bad)

        print("\n=== Test 5: Multiple characters ===")
        Arya = Stark("Arya")
        Jon = Stark("Jon")
        print(Arya.__dict__)
        print(Jon.__dict__)
        Arya.die()
        print("Arya alive?", Arya.is_alive)
        print("Jon alive?", Jon.is_alive)

        print("\n=== Test 6: Empty string for first_name ===")
        empty = None
        try:
            empty = Stark("")  # empty string
        except ValueError as e:
            print("Caught expected error:", e)
        print("Value of empty after exception:", empty)

        print("\n=== All tests passed successfully ===")

    except Exception as e:
        print("UNEXPECTED ERROR:", type(e).__name__, "-", e)


if __name__ == "__main__":
    main()
