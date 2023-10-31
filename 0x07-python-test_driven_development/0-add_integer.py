#!/usr/bin/python3
""" module: adds two integers together """


def add_integer(a, b=98):
    """
       add_intager: adds two integers
        Args:
            a: The first integer
            b: The second integer
        Return:
            The result of a + b
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float] or b is None:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
