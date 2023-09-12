#!/usr/bin/python3
"""
module that writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8) and returns
    the number of characters written
    Args:
        filename: name of file to be writen
        text: string to be written into the file
    Return: number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as myfile:
        return myfile.write(text)
