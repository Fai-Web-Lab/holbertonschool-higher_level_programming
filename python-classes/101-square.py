#!/usr/bin/python3
"""
This module defines a Square class with size, position, and string representation.
"""


class Square:
    """
    Defines a square by size and position.
    Supports area calculation, printing, and string conversion.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.

        Args:
            size (int): The side length of the square.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with tuple validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """
        Defines the string representation of the Square instance.
        Returns the square as a string of # characters with correct positioning.
        """
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"

        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result

    def my_print(self):
        """Prints the square using its string representation."""
        print(self.__str__())
