import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for given lists of heights and weights.
    Calculate BMI with comprehensive error handling.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.

    Raises:
        ValueError: If inputs are not lists of int/float or if sizes mismatch.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("Both height and weight must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be the same length.")

    if len(height) == 0 or len(weight) == 0:
        raise ValueError("Lists cannot be empty.")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError(
                "Height and weight must contain only int or float values."
            )
        if h <= 0 or w <= 0:
            raise ValueError("Height/weight must be greater than 0.")

    height_arr = np.array(height, dtype=float)
    weight_arr = np.array(weight, dtype=float)
    bmi_arr = weight_arr / (height_arr ** 2)

    return bmi_arr.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit check on a list of BMI values.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Threshold value to compare against.

    Returns:
        list[bool]: List of booleans (True if BMI above limit,False otherwise).

    Raises:
        ValueError: If bmi is not a list of int/float or limit is not an int.
    """
    if not isinstance(bmi, list):
        raise ValueError("BMI must be a list.")

    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer.")

    for val in bmi:
        if not isinstance(val, (int, float)):
            raise ValueError("BMI list must contain only int or float values.")
        if val <= 0:
            raise ValueError("BMI values must be greater than 0.")

    return [val > limit for val in bmi]
