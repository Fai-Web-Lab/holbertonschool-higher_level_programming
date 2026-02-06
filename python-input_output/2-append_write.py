#!/usr/bin/python3
"""Module that contains a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
