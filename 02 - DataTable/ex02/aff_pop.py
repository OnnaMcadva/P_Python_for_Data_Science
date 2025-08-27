"""Compare population over time for two countries (1800–2050)."""
from __future__ import annotations

from typing import Iterable, Optional

import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def _years_from_columns(columns: Iterable[str]) -> list[int]:
    years: list[int] = []
    for col in columns:
        try:
            years.append(int(col))
        except ValueError:
            continue
    years.sort()
    return years


def _country_series(df: pd.DataFrame, country: str) -> Optional[pd.Series]:
    if "country" not in df.columns:
        return None
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
    series = pd.to_numeric(series, errors="coerce")
    series.index = years
    series = series.dropna()
    return series


def aff_pop(country1: str = "Czechia", country2: str = "France") -> bool:
    """Plot population of two countries between 1800 and 2050.

    Args:
        country1: First country (campus country).
        country2: Second country for comparison.

    Returns:
        True on success, False otherwise.
    """
    df = load("population_total.csv")
    if df is None:
        return False

    s1 = _country_series(df, country1)
    s2 = _country_series(df, country2)
    if s1 is None or s1.empty:
        print(f"Error: country '{country1}' not found or has no data.")
        return False
    if s2 is None or s2.empty:
        print(f"Error: country '{country2}' not found or has no data.")
        return False

    # Limit to years 1800..2050 (inclusive) if available
    start, end = 1800, 2050
    s1 = s1[(s1.index >= start) & (s1.index <= end)]
    s2 = s2[(s2.index >= start) & (s2.index <= end)]

    plt.figure()
    plt.plot(s1.index, s1.values, label=country1)
    plt.plot(s2.index, s2.values, label=country2)
    plt.title(f"Population: {country1} vs {country2} (1800–2050)")
    plt.xlabel("Year")
    plt.ylabel("Population (people)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
    return True


def main() -> None:
    _ = aff_pop("Czechia", "France")


if __name__ == "__main__":
    main()
