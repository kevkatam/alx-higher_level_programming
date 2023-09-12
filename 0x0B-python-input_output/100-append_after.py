#!/usr/bin/python3
"""
module that contains a function that reads stdin line by line and computes
metrics
"""


def append_after(filename="", search_string="", new_string=""):
    """ function that appends a new line when astring is found
    Args:
        filename: name of file
        search_string: string to search
        new_string: string to append

    """
    result = []
    with open(filename, mode="r", encoding="UTF-8") as my_file:
        for line in my_file:
            result += [line]
            if line.find(search_string) != -1:
                result += [new_string]

    with open(filename, mode="w", encoding="UTF-8") as my_file:
        my_file.write("".join(result))
