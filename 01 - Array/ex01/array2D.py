import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and return a truncated version.

    Args:
        family (list): 2D array to slice
        start (int): Starting index for slicing
        end (int): Ending index for slicing
    Returns:
        list: Truncated 2D array
    Raises:
        ValueError: If input is not a 2D list or has inconsistent dimensions
        TypeError: If start or end are not integers
    """

    if not isinstance(family, list):
        raise ValueError("Input must be a list")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")

    if not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a 2D list")

    if len(family) == 0:
        raise ValueError("Input list cannot be empty")

    first_len = len(family[0])

    if not all(len(row) == first_len for row in family):
        raise ValueError("All rows must have the same number of columns")

    print("* 📚 *")

    arr = np.array(family)
    print(f"My shape is : {arr.shape}")

    sliced_arr = arr[start:end]
    print(f"My new shape is : {sliced_arr.shape}")

    return sliced_arr.tolist()
