#!/usr/bin/python3
# 7-base_geometry.py
"""Provides BaseGeometry with area() and integer_validator()."""


class BaseGeometry:
    """Base class for geometry-related objects."""

    def area(self):
        """Raise an exception because area is not implemented at this level."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): Label used in error messages.
            value (int): Number to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
