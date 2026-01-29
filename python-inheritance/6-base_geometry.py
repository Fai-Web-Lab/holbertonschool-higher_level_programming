#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        This method is intended to be overridden by subclasses.

        Raises:
            Exception: with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
