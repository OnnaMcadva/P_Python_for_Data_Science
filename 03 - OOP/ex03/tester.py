from ft_calculator import calculator


def main():
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        print("Addition test:")
        v1 + 5
        print("---")

        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        print("Multiplication test:")
        v2 * 5
        print("---")

        v3 = calculator([10.0, 15.0, 20.0])
        print("Subtraction test:")
        v3 - 5
        print("Division test:")
        v3 / 5
        print("---")

        v4 = calculator([1, 2, 3])
        print("Test with float scalar:")
        v4 + 2.5
        v4 * 2.5
        v4 - 1.5
        v4 / 0.5
        print("---")

        v5 = calculator([1, 2, 3])
        try:
            v5 / 0
        except ValueError as e:
            print("Caught expected error:", e)

        v6 = calculator([1, 2, 3])
        try:
            v6 + "a"
        except TypeError as e:
            print("Caught expected error:", e)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
