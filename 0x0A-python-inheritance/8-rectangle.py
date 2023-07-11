#!/usr/bin/python3
"""This module represents subclass Rectangle of baseclass BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
    - _width (int): The width of the rectangle.
    - _height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle object.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
