#!/usr/bin/python3
"""
module that inherits from class int and inverts
== and != operators
"""


class MyInt(int):
    """ class that inherits from int """
    def __ne__(self, i):
        """ method that returns == check """
        return int.__eq__(self, i)

    def __eq__(self, i):
        """ method that returns != check """
        return int.__ne__(self, i)
