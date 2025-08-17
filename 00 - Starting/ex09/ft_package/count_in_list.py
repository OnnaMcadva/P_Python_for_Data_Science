"""
count_in_list
=============

This module defines the function `count_in_list` that counts how many times
a given element appears in a list.
"""

from typing import Any, List


def count_in_list(lst: List[Any], element: Any) -> int:
    """
    Count the number of occurrences of `element` in `lst`.

    Args:
        lst (List[Any]): The list in which to search.
        element (Any): The element to count.

    Returns:
        int: The number of times `element` appears in `lst`.

    Raises:
        TypeError: If `lst` is not a list.
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list.")
    return lst.count(element)
