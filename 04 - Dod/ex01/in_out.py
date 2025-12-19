from typing import Callable


def square(x: int | float) -> int | float:
    """Returns x squared."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x exponentiated by itself."""
    return x ** x


def outer(x: int | float, function: Callable) -> object:
    """
    Returns an inner function that applies `function`
    to x repeatedly with internal count increment.
    """
    count = 0

    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner
