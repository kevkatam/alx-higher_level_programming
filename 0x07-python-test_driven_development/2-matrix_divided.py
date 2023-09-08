#!/usr/bin/python3
"""
module containign a function that divides all elements of a matrix by a number
into two decimal places
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix by a number
    Args:
        matrix: list of lists of integers or floats
        div: number
    Return:
        new matrix
    Raises:
        TypeError: if the rows of the matrix are not of the same size
        TypeError: if div is not a number ie integer or float
                   if the elements of the matrix are not lists
                   if the elemts of the lists are not integers
        ZeroDivisionError: if div is a 0
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_t = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_t)
    msg_s = "Each row of the matrix must have the same size"
    _len = 0
    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msg_t)
        if _len != 0 and len(elements) != _len:
            raise TypeError(msg_s)

        for i in elements:
            if not type(i) in (int, float):
                raise TypeError(msg_t)
        _len = len(elements)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
