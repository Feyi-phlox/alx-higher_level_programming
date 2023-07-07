#!/usr/bin/python3
"""This is the add integers module"""


def add_integer(a, b=98):
    """
    Adds two integers and returns their sum.

    Args:
    a: An integer or float.
    b: An integer or float (default is 98).
    return: The addition of a and b as an integer.
    raises TypeError: If a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
