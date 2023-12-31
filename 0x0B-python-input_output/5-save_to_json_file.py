#!/usr/bin/python3
"""Defines a Python obj file writing function"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
