#!/usr/bin/python3
"""
Function that prints a square with the character #.
"""


def print_square(size):
    """
    Checks that size is an integer.
    Throws an error if size isn't an integer.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    """
    Prints #.
    """
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
