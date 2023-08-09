#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
            if ord(str[i]) >= 97 and ord(str[i]) <= 122:
                no = 32
            else:
                no = 0
            print("{:c}".format(ord(str[i]) - no), end="")
    print()
