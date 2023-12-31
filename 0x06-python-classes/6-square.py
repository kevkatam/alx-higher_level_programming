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
        self.position = position

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
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ method that prints the square using character '#' """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
