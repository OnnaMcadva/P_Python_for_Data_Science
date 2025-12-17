class calculator:
    """A calculator for vector operations, including dot"""
    """product, addition, and subtraction."""

    def __init__(self, vector: list = None):
        """Initialize with a vector (optional)."""
        self.vector = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors and print the result."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise and print the resulting vector."""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract the second vector from the first"""
        """element-wise and print the result."""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
