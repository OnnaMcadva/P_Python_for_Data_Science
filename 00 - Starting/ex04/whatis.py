#!/usr/bin/env python3
import sys


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


try:
    if len(sys.argv) == 1:
        exit()
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided🪄")
    elif not is_integer(sys.argv[1]):
        raise AssertionError("argument is not an integer🪄")
    else:
        number = int(sys.argv[1])
        print("🦄 I'm Even." if number % 2 == 0 else "🐳 I'm Odd.")

except AssertionError as e:
    print(f"🪄 AssertionError: {e}")
