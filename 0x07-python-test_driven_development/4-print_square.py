#!/usr/bin/python3
"""
module containing a function that prints a square with the character #
"""


def print_square(size):
    """ function that prints a square with the character #
    Args:
        size: size length of the square
    Raises:
        TypeError: if size is not an integer
                   if size is a float and is less than zero
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
