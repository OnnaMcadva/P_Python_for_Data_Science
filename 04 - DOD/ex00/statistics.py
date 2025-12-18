from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculates statistics (mean, median, quartile, std, var) from *args
    depending on **kwargs values.
    """
    try:
        if len(args) == 0:
            raise ValueError("No data provided")

        numbers = list(map(float, args))
        numbers.sort()

        def mean():
            return sum(numbers) / len(numbers)

        def median():
            n = len(numbers)
            mid = n // 2
            if n % 2 == 0:
                return (numbers[mid - 1] + numbers[mid]) / 2
            return numbers[mid]

        def quartile():
            n = len(numbers)
            q1_index = n // 4
            q3_index = (3 * n) // 4
            return [float(numbers[q1_index]), float(numbers[q3_index])]

        def var():
            m = mean()
            return sum((x - m) ** 2 for x in numbers) / len(numbers)

        def std():
            return var() ** 0.5

        operations = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "var": var,
            "std": std,
        }

        for key in kwargs.values():
            if key in operations:
                print(f"{key} : {operations[key]()}")


    except Exception:
        print("ERROR")
