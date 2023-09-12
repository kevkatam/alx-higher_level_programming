#!/usr/bin/python3
"""
module that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of file to be read
    """
    with open(filename, mode="r", encoding="UTF-8") as myfile:
        print(myfile.read(), end='')
