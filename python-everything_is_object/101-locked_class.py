#!/usr/bin/python3
"""
This module defines a restricted class called LockedClass.
"""


class LockedClass:
    """
    A class that prevents dynamic attribute creation,
    except for 'first_name'.
    """
    __slots__ = ['first_name']
