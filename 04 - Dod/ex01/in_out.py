from typing import Callable, Union


def ft_square(x: Union[int, float]) -> Union[int, float]:
    """Returns x squared."""
    return x * x


def ft_pow(x: Union[int, float]) -> Union[int, float]:
    """Returns x exponentiated by itself."""
    return x ** x


def ft_outer(x: Union[int, float], function: Callable) -> object:
    """
    Returns an inner function that applies `function`
    to x repeatedly with internal count increment.
    """
    count = 0

    def ft_inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return ft_inner
