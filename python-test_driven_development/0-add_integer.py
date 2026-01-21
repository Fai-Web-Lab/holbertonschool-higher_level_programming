#!/usr/bin/python3
"""
This module provides a function for integer addition.
It includes type checking and casting for floats to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats, or are NaN/Inf.

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)) or a != a or abs(a) > 1.7976931348623157e+308:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or abs(b) > 1.7976931348623157e+308:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
