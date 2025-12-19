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
        result = [x + scalar for x in self.vector]
        self.vector = result
        print(self.vector)

    def __mul__(self, scalar: float) -> None:
        """Multiply each element of the vector by a scalar."""
        result = [x * scalar for x in self.vector]
        self.vector = result
        print(self.vector)

    def __sub__(self, scalar: float) -> None:
        """Subtract a scalar from each element of the vector."""
        result = [x - scalar for x in self.vector]
        self.vector = result
        print(self.vector)

    def __truediv__(self, scalar: float) -> None:
        """Divide each element of the vector by a scalar."""
        if scalar == 0:
            raise ZeroDivisionError("division by zero")
        result = [x / scalar for x in self.vector]
        self.vector = result
        print(self.vector)


# class calculator:
#     """A calculator for vector operations, including dot"""
#     """product, addition, and subtraction."""

#     def __init__(self, vector: list = None):
#         """Initialize with a vector (optional)."""
#         self.vector = vector

#     @staticmethod
#     def dotproduct(V1: list[float], V2: list[float]) -> None:
#         """Calculate the dot product of two vectors and print the result."""
#         result = sum(x * y for x, y in zip(V1, V2))
#         print(f"Dot product is: {result}")

#     @staticmethod
#     def add_vec(V1: list[float], V2: list[float]) -> None:
#         """Add two vectors element-wise and print the resulting vector."""
#         result = [float(x + y) for x, y in zip(V1, V2)]
#         print(f"Add Vector is : {result}")

#     @staticmethod
#     def sous_vec(V1: list[float], V2: list[float]) -> None:
#         """Subtract the second vector from the first"""
#         """element-wise and print the result."""
#         result = [float(x - y) for x, y in zip(V1, V2)]
#         print(f"Sous Vector is: {result}")
