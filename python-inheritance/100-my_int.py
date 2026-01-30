#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int
but has inverted == and != operators.
"""


class MyInt(int):
    """
    A rebellious integer class where == and != are swapped.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.
        Returns:
            True if self is not equal to other, otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.
        Returns:
            True if self is equal to other, otherwise False.
        """
        return super().__eq__(other)
