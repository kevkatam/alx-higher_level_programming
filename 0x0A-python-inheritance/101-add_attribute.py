#!/usr/bin/python3
"""
module that adds new attribute to an object if it's possibel
"""


def add_attribute(obj, name, value):
    """ function that  adds a new attribute to an object if it’s possible
    Args:
        obj: object
        name: name of attribute
        value: value of attribute
    Raises:
        TypeError: if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
