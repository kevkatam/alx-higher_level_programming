#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        no = 32
    else:
        no = 0
    print("{:c}".format((i) - no), end="")
