#!/usr/bin/python3
"""
module that contains a function that returns True if the object
is an instance of a class that inherited(directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """ function that returns True if the object
    is an instance of a class that inherited(directly or indirectly)
    from the specified class ; otherwise False
    Args:
        obj: object
        a_class: class type
    Return:
        True if the object is an instance of a class that
        inherited(directly or indirectly)from the specified class ;
        otherwise False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
