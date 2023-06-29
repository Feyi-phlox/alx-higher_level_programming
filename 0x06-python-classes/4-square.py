#!/usr/bin/python3

"""
defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of Square with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2
