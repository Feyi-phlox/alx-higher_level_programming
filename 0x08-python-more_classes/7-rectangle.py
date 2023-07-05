#!/usr/bin/python3
"""This module defines class rectangle"""


class Rectangle:
    """
    Class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of instances of Rectangle.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Optional. The width of the rectangle. Defaults to 0
            height (int): Optional. The height of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get and Returns int: The width of the rectangle.
        """
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
        """Get and returns int: The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args:
            value (int): The new height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and Returns int: The area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and Return int: The perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rcstr = (str(self.print_symbol) * self.__width + "\n")
        rectangle_str = rcstr * self.__height
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate an instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a deletion message when an instance of Rectangle is deleted
        and decrement the number_of_instances attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
