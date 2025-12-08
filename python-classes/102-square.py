#!/usr/bin/python3
"""
This module defines a Square by:
Private instance attribute: size
Instantiation with size
Public instance method that returns the current square area
Square instance that can answer to comparators based on the square area
"""


class Square:
    """
    Defines a square.

    Attributes:
        size (int or float): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size attribute ensuring it is a valid number
        (int or float) and >= 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    # Comparison operators based on area
    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()
