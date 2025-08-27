"""Scatter plot: life expectancy vs GDP per capita (PPP) for year 1900."""
import sys
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def _extract_year_vector(
        df: pd.DataFrame, year: int
        ) -> Optional[pd.DataFrame]:
    """Return a DataFrame with 'country' and the specific year column.

    Ensures the year column exists and is numeric.
    """
    year_col = str(year)
    if "country" not in df.columns or year_col not in df.columns:
        return None
    out = df[["country", year_col]].copy()
    out[year_col] = pd.to_numeric(out[year_col], errors="coerce")
    out = out.dropna(subset=[year_col])
    return out


def projection_life(year: int = 1900) -> bool:
    """Display life expectancy vs GDP per capita for a specific year.

    Args:
        year: Year to display (default: 1900).

    Returns:
        True on success, False otherwise.
    """
    gdp_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_file = "life_expectancy_years.csv"

    gdp = load(gdp_file)
    life = load(life_file)
    if gdp is None or life is None:
        return False

    gdp_y = _extract_year_vector(gdp, year)
    life_y = _extract_year_vector(life, year)
    if gdp_y is None or life_y is None:
        print(f"Error: year {year} not present in both datasets.")
        return False

    merged = pd.merge(
        gdp_y, life_y, on="country", how="inner", suffixes=("_gdp", "_life"))
    if merged.empty:
        print("Error: no overlapping countries for the selected year.")
        return False

    x = merged[str(year) + "_gdp"]
    y = merged[str(year) + "_life"]

    plt.figure()
    plt.scatter(x, y, alpha=0.7, label=str(year))
    plt.title(f"Life expectancy vs GDP per capita (PPP), {year}")
    plt.xlabel("GDP per capita (PPP, inflation-adjusted)")
    plt.ylabel("Life expectancy (years)")
    plt.xscale("log")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return True


def main() -> None:
    try:
        _ = projection_life(1900)
    except Exception as exc:  # noqa: BLE001
        print(f"Unexpected error during test: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
