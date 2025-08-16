#!/usr/bin/env python3
"""Standalone program that counts character categories in a given text.

This program follows the required rules:
- No executable code in the global scope.
- A proper main() guarded by ``if __name__ == "__main__"``.
- All exceptions are caught in main().
- Every function includes a docstring.
- Code respects flake8 style guidelines.
"""

import string
import sys


def count_categories(text: str) -> dict[str, int]:
    """Return counts of character categories in *text*.

    Categories counted are:
      - ``upper``: uppercase letters (``str.isupper``)
      - ``lower``: lowercase letters (``str.islower``)
      - ``punctuation``: ASCII punctuation (``string.punctuation``)
      - ``spaces``: any whitespace (``str.isspace``), including newlines
      - ``digits``: decimal digits (``str.isdigit``)
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }
    punctuation_set = set(string.punctuation)

    for ch in text:
        if ch.isupper():
            counts["upper"] += 1
        elif ch.islower():
            counts["lower"] += 1
        elif ch.isdigit():
            counts["digits"] += 1
        elif ch.isspace():
            counts["spaces"] += 1
        elif ch in punctuation_set:
            counts["punctuation"] += 1
        else:
            # Characters outside the categories are ignored.
            pass

    return counts


def prompt_text() -> str:
    """Prompt the user and read one line *including* the trailing newline.

    The trailing newline (carriage return) is kept so it is counted as a space,
    per the exercise statement. If the user sends EOF (Ctrl+D) immediately,
    an empty string is returned.
    """
    print("What is the text to count?")
    line = sys.stdin.readline()
    if line == "":
        return ""
    return line


def get_text_from_args(argv: list[str]) -> str | None:
    """Extract the text from command-line *argv* according to the rules.

    Returns the text to analyze, or ``None`` to indicate the program should
    prompt the user for input.

    Raises:
        AssertionError: if more than one argument is provided.
    """
    if len(argv) > 2:
        raise AssertionError("more than one argument provided")

    if len(argv) == 2:
        arg = argv[1]
        if arg.lower() == "none":
            return None
        return arg

    return None


def display_counts(text: str) -> None:
    """Print the report of category counts for *text*."""
    counts = count_categories(text)
    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main() -> None:
    """Program entry point with error handling."""
    try:
        text = get_text_from_args(sys.argv)
        if text is None:
            text = prompt_text()
        display_counts(text)
    except AssertionError as exc:
        print(f"AssertionError: {exc}")
    except Exception as exc:
        # Catch-all to comply with the "no uncaught exceptions" rule.
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
