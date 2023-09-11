#!/usr/bin/python3
""" module containing class that inherits from the class list
"""


class MyList(list):
    """ class that inherits list class
    Args:
        list: class list
    """
    def print_sorted(self):
        """ method that prints the sorted list """
        sorted_l = self.copy()
        sorted_l.sort()
        print(sorted_l)
