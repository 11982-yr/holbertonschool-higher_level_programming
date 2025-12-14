#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
