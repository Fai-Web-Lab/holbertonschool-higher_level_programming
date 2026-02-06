#!/usr/bin/python3
"""Module that contains a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The Python object to be serialized and saved.
        filename (str): The name of the file to save to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
