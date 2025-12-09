#!/usr/bin/python3
"""
This module defines a rectangle by:
Private instance attribute: width
Private instance attribute: height
Instantiation with optional width and height
Public instance method that returns the rectangle area
Public instance method that returns the rectangle perimeter
"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle_rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rectangle_rows)

    def __repr__(self):
        """Return a canonical representation of Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
