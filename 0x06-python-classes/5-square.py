#!/usr/bin/python3
"""
module square that defines a square
"""


class Square:
    """ class square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
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

    @property
    def position(self):
        """ method that defines square position from the edge """
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position == value

    def my_print(self):
        """ method that prints the square using character '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
