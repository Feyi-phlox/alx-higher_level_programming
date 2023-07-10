#!/usr/bin/python3
"""This module represents a class MyList the inherits a base class list"""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

    All elements in the list are assumed to be of type int.

    Args:
        list (list): The list to initialize the object.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
