#!/usr/bin/python3
"""
This module defines a Square class with area comparison capabilities.
"""


class Square:
    """
    Defines a square by size and provides comparison methods based on area.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (number): The side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with type (int/float) and value validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
    

    def __eq__(self, other):
        """Compare if two squares are equal in area (==)."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal in area (!=)."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if one square is less than another in area (<)."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square is less than or equal in area (<=)."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if one square is greater than another in area (>)."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square is greater than or equal in area (>=)."""
        return self.area() >= other.area()
