#!/usr/bin/python3
"""
module that contain method that etrieves a dictionary
representation of a Student instance
"""


class Student:
    """ class that retrieves a dictionary representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method that returns dictionary representation of a Student
        instance
        """
        return self.__dict__.copy()
