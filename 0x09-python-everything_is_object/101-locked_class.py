#!/usr/bin/python3
"""
A module containing a class that prevents the user from dynamically creating attributes
"""


class LockedClass:
    __slots__ = ['first_name']

    def __int__(self):
        """ Init method """
        pass
