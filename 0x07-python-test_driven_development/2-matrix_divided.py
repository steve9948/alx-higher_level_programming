#!/usr/bin/python3
""" divides elemtnts of a matrix """


def matrix_divided(matrix, div):
    """
        divides elements of a matrix
        Args:
            matrix: matrix to be divided
            div: number used to divide
        Return:
            matrix with the elements divided
    """
    if not all(isinstance(matrix, list)):
        raise TypeError(
            'matrix must be a matrix (list of lists)of integers/floats'
             )
    """Checks if lists are of the same length """
    it = iter(matrix)
    length = len(next(it))
    if not all(len(l) == length for l in it):
        raise TypeError('Each row of the matrix must have the same size')
    """ validating list values """
    for lst in matrix:
        for num in lst:
            if type(num) not in [int, float] or num is None:
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                     )
    """ checking the div """
    if type(div) not in [int, float] or div is None:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    """ else, matrix division"""
    return([list(map(lambda x: round(x / div, 2), num))for num in matrix])
