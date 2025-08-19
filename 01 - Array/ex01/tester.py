from array2D import slice_me


def main():
    """Test function for slice_me"""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    try:
        slice_me("not a list", 0, 1)
    except ValueError as e:
        print(f"Caught error: {e}")

    try:
        slice_me([[1, 2], [3]], 0, 1)
    except ValueError as e:
        print(f"Caught error: {e}")


if __name__ == "__main__":
    main()
