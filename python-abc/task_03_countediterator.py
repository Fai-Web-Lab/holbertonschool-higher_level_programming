#!/usr/bin/python3
"""
This module defines CountedIterator, a class that tracks the number
of items iterated over from an iterable object.
"""


class CountedIterator:
    """
    An iterator wrapper that maintains a count of fetched items.
    """

    def __init__(self, some_iterable):
        """
        Initializes the CountedIterator.

        Args:
            some_iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(some_iterable)
        self.__count = 0

    def get_count(self):
        """Returns the number of items that have been iterated over."""
        return self.__count

    def __next__(self):
        """
        Increments the counter and returns the next item.

        Raises:
            StopIteration: When there are no more items to fetch.
        """
        try:
            item = next(self.iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration
