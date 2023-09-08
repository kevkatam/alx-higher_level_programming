#!/usr/bin/python3
"""
module containing a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args:
        text: parsed text to be printed
    Raises:
        TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    txt = text[:]
    for i in ".?:":
        listtext = txt.split(i)
        txt = ""
        for j in listtext:
            j = j.strip(" ")
            txt = j + i if txt is "" else txt + "\n\n" + j + i
    print(txt[:-3], end="")
