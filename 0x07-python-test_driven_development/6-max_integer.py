#!/bin/usr/python3
"""This module finds the max integer in a list"""


def max_integer(list=[]):
    """
    Finds the maximum integer from a given list.

    Args:
        list (list): The list of integers.

    Returns:
        int: The maximum integer from the list.

    Raises:
        TypeError: If the list contains elements that are not integers.
    """
    if len(list) == 0:
        return None

    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1

    return result
