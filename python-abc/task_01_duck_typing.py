#!/usr/bin/python3
"""Module containing Shape class and its inheritances"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """The Shape class"""

    @abstractmethod
    def area(self):
        """Method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method for perimeter"""
        pass


class Circle(Shape):
    """The Circle class inherited from Shape"""

    def __init__(self, radius):
        """Initialization wih radius"""
        self.radius = abs(radius)

    def area(self):
        """Returning duck area"""
        return pi * self.radius ** 2

    def perimeter(self):
        """Returning perimeter area"""
        return pi * self.radius * 2


class Rectangle(Shape):
    """The Rectangle class inherited from Shape"""

    def __init__(self, width, height):
        """Initialization wih width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returning duck area"""
        return self.width * self.height

    def perimeter(self):
        """Returning perimeter area"""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Function to give shape info"""

    # Calculating the area and perimeter
    area = obj.area()
    perimeter = obj.perimeter()

    # Printing the area and perimeter
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
