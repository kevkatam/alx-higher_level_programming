#!/usr/bin/python3
"""
module containing a function that adds two numbers
"""


def add_integer(a, b=98):
    """"
    function that adds two integers
    Args:
        a: first integer
        b: second integer
    Return:
        sum of a and b
    Raises:
        TypeError: if a and be are not integers or float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
