#!/usr/bin/python3
"""
This module demonstrates Abstract Base Classes combined with Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle.
    """

    def __init__(self, radius):
        """Initializes circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle using pi * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns perimeter (circumference) of the circle using 2 * pi * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """

    def __init__(self, width, height):
        """Initializes rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle using width * height."""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the rectangle using 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using Duck Typing.

    Args:
        shape: An object expected to have area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
