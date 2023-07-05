#!/usr/bin/python3
"""This module defines Rectangle class"""


class Rectangle:
    """Class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Optional. The width of the rectangle. Defaults to 0.
            height (int): Optional. The height of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and Returns int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        Args:
            value (int): The new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and Returns int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args: value(int)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and Returns int: The area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and Returns int: The perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns str: The string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns str: The string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
