#!/usr/bin/python3
"""class Square """

class Square:
    """
        Square: defines a square
            size: size of square
        Method:
            __init__: init of the size attribute of each instance
    """

    def __init__(self, size=0):
        """ Initialization of attributes for instances
                size: size of the square (int)
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area (self):
        """Area of the square"""
        return self.__size ** 2
