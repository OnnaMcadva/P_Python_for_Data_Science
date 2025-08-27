"""Utility to load CSV datasets with robust error handling.

- Python 3.10
- No globals, explicit imports, PEP8-friendly
- Prints the dataset dimensions exactly as required and returns the DataFrame.
- Returns None on any failure.
"""
from __future__ import annotations

import sys
from typing import Optional

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

    rows, cols = df.shape
    print(f"Loading dataset of dimensions ({rows}, {cols})")
    return df


def main() -> None:
    """Basic smoke tests with safe error handling.

    These are only examples and won't raise if files are missing.
    """
    try:
        # Example smoke test; safe if file doesn't exist.
        _ = load("life_expectancy_years.csv")
    except Exception as exc:  # noqa: BLE001
        # Defensive programming: never crash.
        print(f"Unexpected error during test: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
