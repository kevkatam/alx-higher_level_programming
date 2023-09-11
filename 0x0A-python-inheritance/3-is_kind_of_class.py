#!/usr/bin/python3
"""
module containing a function that returns True if the object is an
instance of, or if the object is an instance of a class that
inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an
    instance of, or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.
    Args:
        obj: objec
        a_class: classtype
    Return:
        True if the object is an
        instance of, or if the object is an instance of a class that
        inherited from, the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
