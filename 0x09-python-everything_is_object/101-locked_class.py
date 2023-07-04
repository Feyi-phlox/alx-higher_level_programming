#!/usr/bin/python3
"""
class that prevents dynamic creation of new instance attribute
"""


class LockedClass:
    """
    class attribute set
    """
    __slots__ = ['first_name']
