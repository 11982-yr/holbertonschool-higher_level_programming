#!/usr/bin/env python3
"""Module defining CountedIterator"""


class CountedIterator:
    """Iterator that counts how many items have been iterated"""

    def __init__(self, iterable):
        """Initialize iterator and counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item and increment counter"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return number of items iterated"""
        return self.count
