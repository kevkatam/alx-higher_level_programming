#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ function that finds peak in a list """
    length = len(list_of_integers)
    mylist = list_of_integers
    x = int(length / 2)
    if mylist == []:
        return (None)
    if x - 1 < 0 and x + 1 >= length:
        return mylist[x]
    elif x - 1 < 0:
        return mylist[x] if mylist[x] > mylist[x + 1] else mylist[x + 1]
    elif x + 1 >= length:
        return mylist[x] if mylist[x] > mylist[x - 1] else mylist[x - 1]
    if mylist[x - 1] < mylist[x] > mylist[x + 1]:
        return (mylist[x])

    if mylist[x + 1] > mylist[x - 1]:
        return find_peak(mylist[x:])
    return find_peak(mylist[:x])
