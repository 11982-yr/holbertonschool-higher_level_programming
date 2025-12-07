#!/usr/bin/python3
"""
This module defines a square by:
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)
Public instance method: def area(self):
that returns the current square area
Public instance method: def my_print(self): 
that prints in stdout the square with the character #
"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
