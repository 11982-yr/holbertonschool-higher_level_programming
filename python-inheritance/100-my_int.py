#!/usr/bin/python3
"""Module defining MyInt class"""


class MyInt(int):
    """Rebel integer class"""

    def __eq__(self, other):
        """Invert == behavior"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Invert != behavior"""
        return int.__eq__(self, other)
