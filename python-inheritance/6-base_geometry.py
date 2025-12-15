#!/usr/bin/python3
"""Defines an empty class named BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
