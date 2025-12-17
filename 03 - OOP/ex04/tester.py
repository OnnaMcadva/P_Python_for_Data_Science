from ft_calculator import calculator


def main():
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        print("Basic test:")
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
        print("---")

        x = [1.5, -2.0, 0]
        y = [3.5, 2.0, -1.0]
        print("Additional test with floats and negatives:")
        calculator.dotproduct(x, y)
        calculator.add_vec(x, y)
        calculator.sous_vec(x, y)
        print("---")

        m = [0, 0, 0]
        n = [1, 2, 3]
        print("Test with zeros:")
        calculator.dotproduct(m, n)
        calculator.add_vec(m, n)
        calculator.sous_vec(m, n)
        print("---")

        p = [1000, 2000, 3000]
        q = [10, 20, 30]
        print("Test with large numbers:")
        calculator.dotproduct(p, q)
        calculator.add_vec(p, q)
        calculator.sous_vec(p, q)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
