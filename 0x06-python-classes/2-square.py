#!/usr/bin/python3

"""This module defines a Square class."""


class Square:

    """defines function __init__"""

    def __init__(self, size=0):

        """Initializes an if statement"""

        if not isinstance(size, int):

            """raises TypeError: If size is not an integer."""

            raise TypeError("size must be an integer")

        if size < 0:

            """raises ValueError: If size is less than 0"""

            raise ValueError("size must be >= 0")
        else:

            """ initialize __size of self with size """
        self.__size = size
