#!/usr/bin/env python3
import sys


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    try:
        if len(sys.argv) == 1:
            return

        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided🪄")

        if not is_integer(sys.argv[1]):
            raise AssertionError("argument is not an integer🪄")

        number = int(sys.argv[1])
        if number % 2 == 0:
            print("🦄 I'm Even.")
        else:
            print("🐳 I'm Odd.")

    except AssertionError as e:
        print(f"🪄 AssertionError: {e}")


if __name__ == "__main__":
    main()
