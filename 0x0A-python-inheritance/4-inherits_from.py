#!/usr/bin/python3
"""This module checks the instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Parameters:
    - obj: An object to check.
    - a_class: The class to compare against.

    Returns: True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
