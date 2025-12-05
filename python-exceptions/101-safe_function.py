#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Execute a function safely.

    Args:
        fct: function to execute.
        *args: arguments to pass to the function.

    Returns:
        The result of fct(*args), or None if an exception occurs.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
