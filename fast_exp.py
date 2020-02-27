#!/usr/bin/env python
"""fast_exp.py

Return fast exponentiation, with a complexity of O(logn) or less."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

def power(a, b):
    # base case
    if (b == 0):
        return 1
    else:
        half_b = b / 2
        half_exp = power(a, half_b)
        result = half_exp * half_exp
        if (b % 2 == 0):
            return result
        else:
           result *= a
           return result


def main():
    try:
        a = (int)(sys.argv[1])
        b = (int)(sys.argv[2])
        if b < 0:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: fast_exp.py [a] [b]")
        print("[a] = base, as any int")
        print("[b] = exponent, as any positive int")
        sys.exit(1)


    print(power(a, b))

if __name__ == "__main__":
    main()
