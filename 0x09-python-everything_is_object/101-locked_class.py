#!/usr/bin/python3
class LockedClass:
    """
    class that prevents dynamic creation of new instance attribute
    """
    __slots__ = ['first_name']
