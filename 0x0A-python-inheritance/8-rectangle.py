#!/usr/bin/python3
"""
a module rectangle that inherits from basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __int__(self, width, height):
        """ method that initializes the instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
