#!/usr/bin/python3
"""This module reprents the object of a specified class"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Parameters:
    - obj: An object to check.
    - a_class: The class to compare against.

    Returns:
    - True if the object is exactly an instance of the specified class;
   otherwise False.

    """
    if type(obj) == a_class:
        return True
    else:
        return False
