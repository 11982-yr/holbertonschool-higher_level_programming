#!/usr/bin/python3
"""
Module 4-print_square
Function that prints a square using '#'
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The length of the square sides.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
