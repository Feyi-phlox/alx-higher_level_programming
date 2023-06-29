#!/usr/bin/python3

"""
defines a Square class.
"""


class Square:
    """
    deifnes function __init__.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of Square with an optional size.

        Args:
            size (int, optional): The size of the square (default is 0).
                Raises:
                    TypeError: If size is not an integer.
                    ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2
