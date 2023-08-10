#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(i))
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
