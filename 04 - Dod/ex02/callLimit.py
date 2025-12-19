from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """Decorator factory to limit the number of function calls."""
    def callLimiter(function: Callable) -> Callable:
        count = 0

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
