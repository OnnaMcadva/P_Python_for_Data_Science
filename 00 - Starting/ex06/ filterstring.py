#!/usr/bin/env python3
"""
Program that filters words from a string based on minimum length.
"""

import sys
from ft_filter import ft_filter


def is_long_word(word: str, n: int) -> bool:
    """Return True if the length of the word is greater than n."""
    return len(word) > n


def filter_words_by_length(text: str, n: int) -> list[str]:
    """Return a list of words from *text* longer than *n* characters.

    Uses ft_filter and a standard function instead of lambda.
    """
    words = text.split()
    return ft_filter(lambda w: is_long_word(w, n), words)


def main():
    """Main program entry point with error handling for arguments."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        result = filter_words_by_length(text, n)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
