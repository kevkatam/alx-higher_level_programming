#!/usr/bin/python3
"""
module containginga function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """ function that returns JSON of a class
    Args:
        obj: instance of a Class
    Return: JSON of a class
    """
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
