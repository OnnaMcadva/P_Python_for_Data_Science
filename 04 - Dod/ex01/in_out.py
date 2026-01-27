
from typing import Callable, Union



def square(x: Union[int, float]) -> Union[int, float]:
    """Returns x squared."""
    return x * x



def pow(x: Union[int, float]) -> Union[int, float]:
    """Returns x exponentiated by itself."""
    return x ** x



def outer(x: Union[int, float], function: Callable) -> object:
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
