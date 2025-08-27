"""Plot life expectancy over time for a given country."""
import sys
from typing import Iterable, Optional
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def _years_from_columns(columns: Iterable[str]) -> list[int]:
    """Extract year columns as integers, ignoring non-year columns."""
    years: list[int] = []
    for col in columns:
        try:
            year = int(col)
            years.append(year)
        except ValueError:
            continue
    years.sort()
    return years


def _country_series(df: pd.DataFrame, country: str) -> Optional[pd.Series]:
    """Return a time series for the given country with year index as int."""
    if "country" not in df.columns:
        return None
    # aliases = {
    #     "czech republic": "czech republic",
    #     "czechia": "czech republic",
    #     "united states": "united states",
    #     "united states of america": "united states",
    #     "spain": "spain",
    #     "france": "france",
    # }
    # key = aliases.get(country.strip().lower(), country.strip().lower())

    key = country.strip().lower()
    row = df[df["country"].str.strip().str.lower() == key]
    if row.empty:
        return None

    years = _years_from_columns(df.columns)
    if not years:
        return None

    series = row.iloc[0][list(map(str, years))]
    series = pd.to_numeric(series, errors="coerce")
    series.index = years
    series = series.dropna()
    return series


def aff_life(
        country: str = "Spain",
        filename: str = "life_expectancy_years.csv") -> bool:
    """Load dataset and display life expectancy curve for a country.

    Args:
        country: Country name to plot (default: "Spain").
        filename: Path to the CSV file (default: "life_expectancy_years.csv").

    Returns:
        True on success, False if the operation couldn't be completed.
    """
    df = load(filename)
    if df is None:
        return False

    s = _country_series(df, country)
    if s is None or s.empty:
        print(f"Error: country '{country}' not found or has no data.")
        return False

    plt.figure()
    plt.plot(np.array(s.index), np.array(s.values), label=country)
    plt.title(f"Life expectancy in {country}")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy (years)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
    return True


def main() -> None:
    try:
        _ = aff_life("Spain")
    except Exception as exc:  # noqa: BLE001
        print(f"Unexpected error during test: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
