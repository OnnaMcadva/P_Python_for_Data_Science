"""
Test script for ft_package.
"""

from ft_package import count_in_list


def main():
    """
    Main test function with error handling.
    """
    try:
        print(count_in_list(["toto", "tata", "toto"], "toto"))  # Expected: 2
        print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Expected: 0
        print(count_in_list("not_a_list", "toto"))  # Should raise TypeError
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
