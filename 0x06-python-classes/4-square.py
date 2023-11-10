#!/usr/bin/python3
"""
module square that defines a square
"""


class Square:
    """ class square that defines a square """

    def __init__(self, size=0):
        """ method that initializes th attribute size of the square

        Args:
            size: size of the square(int)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    @property
    def size(self):
        """ retrieves size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ method that sets the value of size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method that returns the current square area """
        return (self.__size * self.__size)
