#!/usr/bin/python3
"""
a module rectangle that inherits from basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class that defines a rectangle from the basegeometry class """
    def __init__(self, width, height):
        """ method that initializes the instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self, width, height):
        """ method that prints the area of a rectangle """
        return (self.___width * self.__height)

    def __str__(self, width, height):
        """ method that returns formated string using __str__ magic """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
