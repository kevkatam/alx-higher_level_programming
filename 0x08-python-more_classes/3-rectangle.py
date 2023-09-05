#!/usr/bin/python3
"""
Module composed of a class thaat defines a rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width
        Args:
            value: width
        Returns:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Args:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Returns:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method that returns the rectangle area
        Return:
            area of the rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """ method that returns the perimeter of the rectangle
        Return:
            perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """ method that returns the rectangle #
        Returns:
            str of th rectangle
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return (rectangle)
        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"
        return (rectangle[:-1])
