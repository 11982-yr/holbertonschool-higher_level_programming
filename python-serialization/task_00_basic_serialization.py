#!/usr/bin/python3
"""Basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    If the file exists, it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file
    and return it as a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
