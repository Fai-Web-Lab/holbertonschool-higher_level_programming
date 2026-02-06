#!/usr/bin/python
"""Module that contains a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of chars.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
