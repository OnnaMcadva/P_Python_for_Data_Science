"""Plot life expectancy over time for a given country (campus country)."""
from __future__ import annotations

from typing import Iterable, Optional

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
    # Case-insensitive match with support for common synonyms
    aliases = {
        "czech republic": "czech republic",
        "czechia": "czech republic",
        "united states": "united states",
        "united states of america": "united states",
    }
    key = aliases.get(country.strip().lower(), country.strip().lower())

    row = df[df["country"].str.strip().str.lower() == key]
    if row.empty:
        return None

    years = _years_from_columns(df.columns)
    if not years:
        return None

    series = row.iloc[0][list(map(str, years))]
    # Convert to numeric and drop missing values
    series = pd.to_numeric(series, errors="coerce")
    series.index = years
    series = series.dropna()
    return series


def aff_life(country: str = "Czechia") -> bool:
    """Load dataset and display life expectancy curve for a country.

    Args:
        country: Country name to plot (default: "Czechia").

    Returns:
        True on success, False if the operation couldn't be completed.
    """
    df = load("life_expectancy_years.csv")
    if df is None:
        return False

    s = _country_series(df, country)
    if s is None or s.empty:
        print(f"Error: country '{country}' not found or has no data.")
        return False

    plt.figure()
    plt.plot(s.index, s.values, label=country)
    plt.title(f"Life expectancy in {country}")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy (years)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
    return True


def main() -> None:
    # Choose your campus country here; change if needed.
    # Default set to Czechia to match Prague timezone.
    _ = aff_life("Czechia")  # Try "Czech Republic" if your CSV uses that name.


if __name__ == "__main__":
    main()
