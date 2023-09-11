#!/usr/bin/python3
"""
module that raises an exception
"""


class BaseGeometry:
    """ empty class """
    def area(self):
        """ method that raises an exception
        """
        raise Exception("area() is not implemented")
