#!/usr/bin/python3
"""
module containing a function that  writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj: object
        filename: text file the object is written into
    """
    with open(filename, "w", encoding="UTF-8") as myfile:
        json.dump(my_obj, myfile)
