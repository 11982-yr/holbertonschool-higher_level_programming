#!/usr/bin/python3
"""
This module defines a square by:
Private instance attribute: size
Instantiation with optional size
"""


class Square:
  """Represents a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
