#!/usr/bin/python3
"""
module that raises an exception
"""


class BaseGeometry:
    def area(self):
        """ method that raises an exception
        """
        raise Exception("area() is not implemented")
