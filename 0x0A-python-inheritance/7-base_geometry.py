#!/usr/bin/python3
"""
module that raises an exception and validates value
"""


class BaseGeometry:
    """ class that defines the attributes of geometric shapes """
    def area(self):
        """ method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that receives the value property
        Args:
            name: object name
            value: property value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
