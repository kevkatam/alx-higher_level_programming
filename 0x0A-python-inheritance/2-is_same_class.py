#!/usr/bin/python3
"""
module that returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly an instance
    of the specified class ; otherwise False
    Args:
        obj: instance
        a_class: class that obj maybe a n instance of
    Return: True if the object is exactly an instance
        of the specified class ; otherwise False
    """
    return type(obj) is a_class
