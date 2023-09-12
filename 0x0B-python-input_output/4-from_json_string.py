#!/usr/bin/python3
"""
module that contains a function that returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ function that returns an object
    (Python data structure) represented by a JSON string
    Args:
        my_str: json represantation
    Return: object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
