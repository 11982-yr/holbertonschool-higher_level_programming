#!/usr/bin/python3
"""
This module provides the function: add_integer(a, b=98)
It returns the addition of a and b.
"""


def add_integer(a, b=98):
    """
    Calculate the sum of two values and return the result as an integer.

    Parameters:
        a: first number, must be an int or float
        b: second number, defaults to 98, must be int or float

    Raises:
        TypeError: if either a or b is not a number

    The function converts floating-point arguments to integers
    before performing the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
