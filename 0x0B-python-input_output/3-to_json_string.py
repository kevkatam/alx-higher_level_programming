#!/usr/bin/python3
"""
module containging a function that returns the JSON
representation of an object (string)
"""


def to_json_string(my_obj):
    """ function that returns the JSON
    representation of an object (string)
    Args:
        my_obj: object
    """
    return json.dumps(my_obj)
