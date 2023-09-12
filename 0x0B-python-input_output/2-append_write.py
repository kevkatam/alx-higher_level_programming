#!/usr/bin/python3
"""
module containging a function that appends a string at the end
of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ function that appends a string at the end
    of a text file (UTF8) and returns the number of characters added
    Args:
        filaname: name of file to be appended
        text: text to be appended into file
    """
    with open(filename, mode="a", encoding="UTF-8") as myfile:
        return myfile.write(text)
