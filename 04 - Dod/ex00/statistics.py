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
            """Calculate Q1 and Q3 using linear interpolation."""
            n = len(numbers)

            q1_pos = (n - 1) * 0.25
            q1_lower = int(q1_pos)
            q1_upper = q1_lower + 1
            q1_weight = q1_pos - q1_lower

            if q1_upper < n and q1_weight > 0:
                q1 = numbers[q1_lower] * (1 - q1_weight)
                + numbers[q1_upper] * q1_weight
            else:
                q1 = numbers[q1_lower]

            q3_pos = (n - 1) * 0.75
            q3_lower = int(q3_pos)
            q3_upper = q3_lower + 1
            q3_weight = q3_pos - q3_lower

            if q3_upper < n and q3_weight > 0:
                q3 = numbers[q3_lower] * (1 - q3_weight)
                + numbers[q3_upper] * q3_weight
            else:
                q3 = numbers[q3_lower]

            return [float(q1), float(q3)]

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
