#!/usr/bin/python3
"""Defines a Python obj creating function"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: filename
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
