#!/usr/bin/python3
"""This module list of available attributes and methods of an object"""


def lookup(obj):
    """represents a function that list the available attributes and methods

    Args:
        obj (object)

    Returns:
        list: list of attributes and methods
    """
    return list(dir(obj))
