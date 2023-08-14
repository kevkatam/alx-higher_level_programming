#!usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    j = len(my_list) - 1
    while i < j:
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp
        i += 1
        j -= 1
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))
