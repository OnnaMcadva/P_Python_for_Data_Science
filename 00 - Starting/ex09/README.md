# ft_package

A sample test package for counting occurrences in a list.

## Installation

You can install the package using pip:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

# Example usage
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
