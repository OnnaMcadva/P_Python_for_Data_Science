class calculator:
    """A calculator class for vector operations with a scalar."""

    def __init__(self, vector: list):
        """Initialize the calculator with a vector of numbers."""
        if not isinstance(vector, list) or not all(
            isinstance(x, (int, float)) for x in vector
        ):
            raise ValueError("Vector must be a list of numbers")
        self.vector = vector

    def __add__(self, scalar: float) -> None:
        """Add a scalar to each element of the vector."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only add a numeric scalar")
        result = [x + scalar for x in self.vector]
        print(result)

    def __mul__(self, scalar: float) -> None:
        """Multiply each element of the vector by a scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a numeric scalar")
        result = [x * scalar for x in self.vector]
        print(result)

    def __sub__(self, scalar: float) -> None:
        """Subtract a scalar from each element of the vector."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only subtract a numeric scalar")
        result = [x - scalar for x in self.vector]
        print(result)

    def __truediv__(self, scalar: float) -> None:
        """Divide each element of the vector by a scalar."""
        """Raises error on division by zero."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only divide by a numeric scalar")
        if scalar == 0:
            raise ValueError("Division by zero is not allowed")
        result = [x / scalar for x in self.vector]
        print(result)
