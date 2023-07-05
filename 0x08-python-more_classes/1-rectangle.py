#!/usr/bin/python3
"""
class the represents a Rectangle
"""


class Rectangle:
    """Rectangle Attributes"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance width and height. """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get and returns the width of the rectangle """
        return self._width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get and returns the height of the rectangle """
        return self._height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
