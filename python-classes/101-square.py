#!/usr/bin/python3
"""
This module defines the Square class with size, position,
area calculation, and printing behavior.
"""


class Square:
    """
    Defines a square with size and position.

    Attributes:
        size (int): The length of a side of the square.
        position (tuple): Position offset for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute ensuring it is a valid integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position attribute ensuring it's a tuple
        of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' considering its position."""
        if self.__size == 0:
            print("")
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print("")

        # Print square lines
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Return the printable representation of the square.
        Works exactly like my_print(), but returns a string.
        """
        if self.__size == 0:
            return ""

        lines = []

        # Vertical offset
        for _ in range(self.__position[1]):
            lines.append("")

        # Square rows
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
