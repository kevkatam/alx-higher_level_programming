#!/usr/bin/python3
"""
A module containging a class that prevents the user from dynamically creating
new instance attributes, except if the new instance attkribute is
called first_name.
"""


class LockedClass:
    __slots__ = ['first_name']

    def __int__(self):
        """ init method """
        pass
