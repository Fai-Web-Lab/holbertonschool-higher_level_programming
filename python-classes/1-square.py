#!/usr/bin/python3
"""
Module defines a class Square with a private instance attribute.
"""


class Square:
    """
    Square by its size.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with a specific size.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
