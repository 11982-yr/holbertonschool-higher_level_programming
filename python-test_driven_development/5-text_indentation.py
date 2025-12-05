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

    separators = ".?:"
    line = ""
    i = 0

    while i < len(text):
        c = text[i]

        if c == '\n':
            # print current collected line without leading spaces
            print(line.lstrip())
            line = ""
            print()   # keep the blank line caused by '\n'
            i += 1
            continue

        # add current character to the current line
        line += c

        if c in separators:
            # print line (with separator), no leading spaces
            print(line.lstrip())
            print()   # extra blank line
            line = ""

        i += 1

    # print remaining text if any (no extra newline at the end)
    if line.strip() != "":
        print(line.lstrip(), end="")
