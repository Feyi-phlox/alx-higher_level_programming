#!/usr/bin/python3
"""This module checks the instance of an object"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Parameters:
    - obj: An object to check.
    - a_class: The class to compare against.

    Returns:True if the object is an instance of
    otherwise, False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
