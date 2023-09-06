#!/usr/bin/python3
"""
module containing an algorithm that solves the  N queens puzzle
using backtracking
"""


def is_secure(mqueen, nqueen):
    """" method that determines if the queens can or can't kill each other

    Args:
        mqueen: array containing yhe position of the queen
        nqueen: queen number
    Return:
        True: when queens can't kill each other
        Fales: when some of the queens can kill each other
    """
    for i in range(nqueen):
        if mqueen[i] == mqueen[nqueen]:
            return False
        if abs(mqueen[i] - mqueen[nqueen]) == abs(i - nqueen):
            return False
    return True


def printresult(mqueen, nqueen):
    """ method that prints the list with the queen's positions
    Args:
        mqueen: array containing yhe position of the queen
        nqueen: queen number
    """
    result = []
    for i in range(nqueen):
        result.append([i, mqueen[i]])
    print(result)


def Queen(mqueen, nqueen):
    """ recursive function that performs the backtracking algorithm
    Args:
        mqueen: array containing yhe position of the queen
        nqueen: queen number
    """
    if nqueen is len(mqueen):
        printresult(mqueen, nqueen)
        return
    mqueen[nqueen] = -1

    while ((mqueen[nqueen] < len(mqueen) - 1)):
        mqueen[nqueen] += 1
        if is_secure(mqueen, nqueen) is True:
            if nqueen is not len(mqueen):
                Queen(mqueen, nqueen + 1)


def resolveNqueen(size):
    """ function that calls the backtracking algo
    Args:
        size: size of the chessboard
    """
    mqueen = [-1 for i in range(size)]
    Queen(mqueen, 0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    resolveNqueen(size)
