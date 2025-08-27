"""Utility to load CSV datasets with robust error handling.

- Python 3.10
- No globals, explicit imports, PEP8-friendly
- Prints the dataset dimensions exactly as required and returns the DataFrame.
- Returns None on any failure.
"""
from typing import Optional
import sys
import pandas as pd


def load(path: str) -> Optional[pd.DataFrame]:
    """Load a CSV dataset and print its dimensions.

    Args:
        path: Path to the CSV file.

    Returns:
        A pandas DataFrame if successful, otherwise None.
    """
    try:
        if not isinstance(path, str) or not path.strip():
            print("Error: path must be a non-empty string.")
            return None

        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: file not found '{path}'.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: empty data file '{path}'.")
        return None
    except pd.errors.ParserError:
        print(f"Error: could not parse CSV '{path}'.")
        return None
    except UnicodeDecodeError:
        print(f"Error: text encoding issue while reading '{path}'.")
        return None
    except Exception as exc:  # noqa: BLE001 - keep broad except for robust CLI
        print(f"Error: {exc}")
        return None

    if "country" not in df.columns:
        print("Error: CSV missing 'country' column.")
        return None

    year_columns = [c for c in df.columns if c.isdigit()]
    if not year_columns:
        print("Error: CSV has no numeric year columns.")
        return None

    if df.empty:
        print("Error: CSV file is empty.")
        return None

    rows, cols = df.shape
    print(f"Loading dataset of dimensions ({rows}, {cols})")
    return df


def main() -> None:
    """Basic smoke tests with safe error handling."""
    try:
        df = load("life_expectancy_years.csv")
        if df is not None:
            print(df)
    except Exception as exc:  # noqa: BLE001
        print(f"Unexpected error during test: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
