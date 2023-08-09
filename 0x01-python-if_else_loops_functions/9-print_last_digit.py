#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    else:
        number = number
    i = number % 10
    print(i, end="")
    return i
