#!/usr/bin/python3
"""
module that contains a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
    Args:
        filname: name of file json file is crated from
    """
    with open(filename, mode="r", encoding="UTF-8") as myfile:
        return json.load(myfile)
