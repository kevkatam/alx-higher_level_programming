#!/usr/bin/python3
def subtract(list_n):
    sub = 0
    maxlist = max(list_n)

    for n in list_n:
        if maxlist > n:
            sub += n
    return (maxlist - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_k = list(rom.keys())

    i = 0
    last = 0
    list_n = [0]

    for c in roman_string:
        for r in list_k:
            if r == c:
                if rom.get(c) <= last:
                    i += subtract(list_n)
                    list_n = [rom.get(c)]
                else:
                    list_n.append(rom.get(c))
                last = rom.get(c)
    i += subtract(list_n)
    return (i)
