#!/usr/bin/python3
"""
module MyList that inherits from list prints the list, but sorted
(ascending sort)
"""


class MyList(list):
    def print_sorted(self):
        """ method that prints the sorted list
        """
        sorted_l = self.copy()
        sorted_l.sort()
        print(sorted_l)
