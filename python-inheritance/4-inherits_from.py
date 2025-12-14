#!/usr/bin/python3
"""Determine whether an object comes from a subclass of a given class."""


def inherits_from(obj, a_class):
    """Return True when obj is an instance of a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
