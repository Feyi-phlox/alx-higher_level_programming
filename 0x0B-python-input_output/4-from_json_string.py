#!/usr/bin/python3
# 6-from_json_string.py
"""This module defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.load(my_str)
