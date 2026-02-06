#!/usr/bin/python3
"""Module contains function to return the dictionary description of an obj."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
