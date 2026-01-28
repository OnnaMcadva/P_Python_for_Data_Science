from statistics import ft_statistics


def main():
    print("=" * 50)
    print("TEST 1: Basic tests from assignment")
    print("=" * 50)
    ft_statistics(1, 42, 360, 11, 64, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    
    print("\n" + "=" * 50)
    print("TEST 2: Single element")
    print("=" * 50)
    ft_statistics(42, a="mean", b="median", c="quartile", d="std", e="var")
    
    print("\n" + "=" * 50)
    print("TEST 3: Two elements")
    print("=" * 50)
    ft_statistics(10, 20, a="mean", b="median", c="quartile")
    
    print("\n" + "=" * 50)
    print("TEST 4: Even number of elements (median = float)")
    print("=" * 50)
    ft_statistics(1, 2, 3, 4, a="median", b="mean")
    
    print("\n" + "=" * 50)
    print("TEST 5: Odd number of elements (median = int)")
    print("=" * 50)
    ft_statistics(1, 2, 3, 4, 5, a="median", b="mean")
    
    print("\n" + "=" * 50)
    print("TEST 6: Negative numbers")
    print("=" * 50)
    ft_statistics(-10, -5, 0, 5, 10, a="mean", b="median", 
                  c="quartile", d="std", e="var")
    
    print("\n" + "=" * 50)
    print("TEST 7: Floating point numbers")
    print("=" * 50)
    ft_statistics(1.5, 2.7, 3.2, 4.8, 5.1, a="mean", b="median", c="quartile")
    
    print("\n" + "=" * 50)
    print("TEST 8: Identical numbers")
    print("=" * 50)
    ft_statistics(5, 5, 5, 5, 5, a="mean", b="median", 
                  c="quartile", d="std", e="var")
    
    print("\n" + "=" * 50)
    print("TEST 9: Large dataset")
    print("=" * 50)
    ft_statistics(*range(1, 101), a="mean", b="median", c="quartile")
    
    print("\n" + "=" * 50)
    print("TEST 10: All operations at once")
    print("=" * 50)
    ft_statistics(10, 20, 30, 40, "50", 
                  op1="mean", op2="median", op3="quartile", 
                  op4="std", op5="var")
    
    print("\n" + "=" * 50)
    print("TEST 11: Unsorted data")
    print("=" * 50)
    ft_statistics(100, 1, 50, 25, 75, a="median", b="quartile")
    
    print("\n" + "=" * 50)
    print("TEST 12: Only kwargs without args (all ERROR)")
    print("=" * 50)
    ft_statistics(a="mean", b="median", c="quartile", d="std", e="var")
    
    print("\n" + "=" * 50)
    print("TEST 13: Only args without kwargs (nothing prints)")
    print("=" * 50)
    ft_statistics(1, 2, 3, 4, 5)
    print("(nothing should be printed)")
    
    print("\n" + "=" * 50)
    print("TEST 14: Mix of correct and incorrect operations")
    print("=" * 50)
    ft_statistics(1, 2, 3, 4, 5, 
                  good1="mean", 
                  bad1="average", 
                  good2="median", 
                  bad2="middle",
                  good3="std")
    
    print("\n" + "=" * 50)
    print("TEST 15: Very large numbers")
    print("=" * 50)
    ft_statistics(1000000, 2000000, 3000000, 4000000, 5000000,
                  a="mean", b="std", c="var")
    
    print("\n" + "=" * 50)
    print("TEST 16: Very small numbers")
    print("=" * 50)
    ft_statistics(0.001, 0.002, 0.003, 0.004, 0.005,
                  a="mean", b="median", c="quartile")
    
    print("\n" + "=" * 50)
    print("TEST 17: Three elements (quartile check)")
    print("=" * 50)
    ft_statistics(1, 2, 3, a="quartile", b="median")
    
    print("\n" + "=" * 50)
    print("TEST 18: Extreme values")
    print("=" * 50)
    ft_statistics(-1000, -1, 0, 1, 1000, 
                  a="mean", b="median", c="quartile", d="std")
    
    print("\n" + "=" * 50)
    print("TEST 19: Repeated operations")
    print("=" * 50)
    ft_statistics(10, 20, 30, 
                  op1="mean", op2="mean", op3="mean", 
                  op4="median", op5="median")
    
    print("\n" + "=" * 50)
    print("TEST 20: Seven elements (classic example)")
    print("=" * 50)
    ft_statistics(2, 4, 6, 8, 10, 12, 14, 
                  a="mean", b="median", c="quartile", d="std", e="var")


    # Additional edge-case tests
    print("\n" + "=" * 50)
    print("TEST 21: Non-numeric input")
    print("=" * 50)
    try:
        ft_statistics(1, "a", 3, test="mean")
    except Exception as e:
        print("Exception:", e)

    print("\n" + "=" * 50)
    print("TEST 22: Infinite and NaN values")
    print("=" * 50)
    try:
        ft_statistics(float('inf'), 1, 2, test="mean")
        ft_statistics(float('-inf'), 1, 2, test="mean")
        ft_statistics(float('nan'), 1, 2, test="mean")
    except Exception as e:
        print("Exception:", e)

    print("\n" + "=" * 50)
    print("TEST 23: Empty input")
    print("=" * 50)
    ft_statistics()

    print("\n" + "=" * 50)
    print("TEST 24: Only one element")
    print("=" * 50)
    ft_statistics(42, test="std", test2="var")

    print("\n" + "=" * 50)
    print("TEST 25: Very large dataset")
    print("=" * 50)
    ft_statistics(*range(100000), test="mean")

    print("\n" + "=" * 50)
    print("TEST 26: Floating point precision")
    print("=" * 50)
    ft_statistics(0.1, 0.2, 0.3, test="mean")


if __name__ == "__main__":
    main()


# from statistics import ft_statistics


# def main():
#     ft_statistics(1, 42, 360, 11, 64, toto="mean",
#                   tutu="median", tata="quartile")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   hello="std", world="var")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   ejfhhe="heheh", ejdjdejn="kdekem")
#     print("-----")
#     ft_statistics(toto="mean", tutu="median", tata="quartile")


# if __name__ == "__main__":
#     main()
