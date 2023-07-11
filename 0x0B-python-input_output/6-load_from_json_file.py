#!/usr/bin/python3
"""This module defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """creates a python object from JSON file"""
    return json.load(filename)
