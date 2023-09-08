#!/usr/bin/python3
"""
mdoule that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """ function that prints first name and last name
    Args:
        first_name: first name entered
        last_name: last name entered
    Raises:
        TypeError: if first_name and last_name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
