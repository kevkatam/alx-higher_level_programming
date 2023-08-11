#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sign = argv[2]
    if sign != '+' and sign != '-' and sign != '*' and sign != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])
    if sign == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sign == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif sign == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
