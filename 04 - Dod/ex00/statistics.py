from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate statistics from given arguments."""
    operations = {}

    if len(args) != 0:
        numbers = list(map(float, args))
        numbers.sort()

        def mean():
            """Calculate mean."""
            result = sum(numbers) / len(numbers)
            return int(result) if result % 1 == 0 else result

        def median():
            """Calculate median."""
            n = len(numbers)
            mid = n // 2
            if n % 2 == 0:
                result = (numbers[mid - 1] + numbers[mid]) / 2
            else:
                result = numbers[mid]
            return int(result) if result % 1 == 0 else result

        def quartile():
            """Calculate inclusive quartiles (Q1 and Q3)."""
            n = len(numbers)
            mid = n // 2

            if n % 2 == 0:
                lower_half = numbers[:mid]
                upper_half = numbers[mid:]
            else:
                lower_half = numbers[:mid + 1]
                upper_half = numbers[mid:]

            def median(data):
                m = len(data)
                mid = m // 2
                if m % 2 == 0:
                    return (data[mid - 1] + data[mid]) / 2
                return data[mid]

            return [float(median(lower_half)), float(median(upper_half))]

        def var():
            """Calculate variance."""
            m = mean()
            return sum((x - m) ** 2 for x in numbers) / len(numbers)

        def std():
            """Calculate standard deviation."""
            return var() ** 0.5

        operations = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "var": var,
            "std": std,
        }

    for value in kwargs.values():
        if value in operations:
            print(f"{value} : {operations[value]()}")
        else:
            print("ERROR")
