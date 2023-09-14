#!/usr/bin/python3
"""
a module base that is base of all the other clases, goal of it
is to manage id attribute in all  and to avoid duplicating the same code
"""


class Base:
    """ class base that is "base" of all other classes in the project
    """
    __nb_objects = 0

    def __int__(self, id=None):
        """ initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
