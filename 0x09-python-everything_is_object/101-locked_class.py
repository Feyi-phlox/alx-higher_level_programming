#!/usr/bin/python3
class LockedClass:
    """
    class that prevents dynamic creation of new instance attribute
    """
    __slots__ = ['first_name']

    def __setattr__(self, key, value):
        """
        Replaces the default attribute assignment behaviour

        agrs:
            key(str): name of attribute
            value(any): value assigned to the attribute
        raises:
            AttributeError: if attribute is not 'first_name'
        """
        if name != 'first_name':
            raise AttributeError("new instance attribute not allowed")
        object.__setattr__(self, key, value)
