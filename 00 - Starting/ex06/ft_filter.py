#!/usr/bin/env python3
"""
Custom implementation of the built-in filter function using list comprehension.
"""

from typing import Callable, Iterable, TypeVar, List

T = TypeVar("T")


def ft_filter(function: Callable[[T], bool], iterable: Iterable[T]) -> List[T]:
    """
    Return a list of items from *iterable* for which *function(item)* is True.

    Args:
        func.(Callable[[T], bool]): A func. returning True/False for each elem.
        iterable (Iterable[T]): Any iterable object.

    Returns:
        List[T]: List of elements where function returns True.
    """
    return [item for item in iterable if function(item)]
