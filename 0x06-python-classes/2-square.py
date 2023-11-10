#!/usr/bin/python3
"""
module square that defines a square
"""


class Square:
    """ class square that defines a square """

    def __init__(self, size):
        """ method that initializes th attribute size of the square

        Args:
            size: size of the square(int)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
