#!/usr/bin/python3
def max_integer(my_list=[]):
    len_my_list = len(my_list)
    if len_my_list == 0:
        return (None)
    maxx = my_list[0]
    for i in range(1, len_my_list):
        if my_list[i] > maxx:
            maxx = my_list[i]
    return (maxx)
