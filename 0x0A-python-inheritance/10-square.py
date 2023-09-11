#!/usr/bin/python3
"""
module square that inherits from class rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ method that finds the square given size """
    def __init__(self, size):
        """ initializes """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ method that returns the area of the square """
        return super().area()

    def __str__(self):
        """ method that returns printable string """
        return ("[Rectangle {}/{}".format(self.__size, self.__size))
