#!/usr/bin/python3
"""Module that contains a function to create an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        any: The Python object represented by the JSON file content.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
