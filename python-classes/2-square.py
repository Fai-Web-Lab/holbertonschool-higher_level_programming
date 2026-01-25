#!/usr/bin/python3
"""
This module defines a Square class with type and value validation.
"""


class Square:
    """
    Defines a square by its size with strict validation.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
