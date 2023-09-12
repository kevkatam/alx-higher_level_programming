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

    def to_json(self, attrs=None):
        """ method that returns dictionary representation of a Student
        instance
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj
            my_dict = {}
            for i in range(len(attrs)):
                for j in obj:
                    if attrs[i] == j:
                        my_dict[j] = obj[j]
            return my_dict
        return obj

    def reload_from_json(self, json):
        """ method that that replaces all attributes of the Student
        instance """
        for i in json:
            self.__dict__[i] = json[i]
