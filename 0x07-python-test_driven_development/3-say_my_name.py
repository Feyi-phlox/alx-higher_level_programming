#!/usr/bin/python3
"""This module defines say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If the first_name or last_name is not a string.

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        if first_name == "":
            print("My name is {}".format(last_name))
            return
        print("My name is {} {}".format(first_name, last_name))
