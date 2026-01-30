#!/usr/bin/python3
"""
This module defines an abstract class Shape and concrete subclasses
Circle and Rectangle to demonstrate Duck Typing and ABCs.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class representing a geometric shape.
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
        """Initializes Circle with radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle: pi * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle: 2 * pi * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle: width * height."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle: 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using Duck Typing.

    Args:
        shape: An object that is expected to have area() and perimeter()
               methods, regardless of its class hierarchy.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
