#!/usr/bin/python3
"""This module defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """creates a python object from JSON file"""
    with open(filename) as filename:
        return json.load(filename)
