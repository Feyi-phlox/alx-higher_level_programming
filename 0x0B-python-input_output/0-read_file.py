#!/usr/bin/python3
"""This module defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as UTF8:
        read_data = UTF8.read()
        print(read_data, end="")
