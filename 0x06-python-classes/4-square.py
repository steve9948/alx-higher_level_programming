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

    @property
    def size(self):
        """ getter to private attribute size
            Return:
                size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for private attribute size
            Args:
                value (int): value to be set
            Return:
                nothing
        """
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
             Square`s area.
        """
        return self.__size * self.__size
