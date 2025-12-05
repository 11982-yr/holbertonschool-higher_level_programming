#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    result = ""
    buffer = ""

    for c in text:
        buffer += c
        if c in chars:
            # Print the collected buffer without leading/trailing spaces
            print(buffer.strip())
            print()
            buffer = ""

    # Print remaining text if any
    if buffer.strip():
        print(buffer.strip(), end="")
