#!/usr/bin/python3
"""
module that contains a function that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ function that returns a list of lists of
    integers representing the Pascal’s triangle of n
    Args:
        n: no of lists
    """

    my_list = []
    p = []
    for i in range(n):
        result = []
        p1 = -1
        p2 = 0
        for j in range(len(p) + 1):
            if p1 == -1 or p2 == len(p):
                result.append(1)
            else:
                result.append(p[p1] + p[p2])
            p1 += 1
            p2 += 1
        my_list.append(result)
        p = result[:]

    return my_list
