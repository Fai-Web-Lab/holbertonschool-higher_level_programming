#!/usr/bin/python3
"""
This module defines an abstract base class Animal and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class representing an Animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a Dog.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a Cat.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
