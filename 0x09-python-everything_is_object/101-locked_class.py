#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("new instance attribute not allowed")
        object.__setattr__(self, name, value)
