#!/usr/bin/python3
"""
Defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    Float arguments are typecast to ints before addition.

    Raises:
        TypeError: If either a or b is not an integer or float,
        or cannot be converted to an integer (e.g. NaN, inf).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle NaN and infinity before int conversion
    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b
