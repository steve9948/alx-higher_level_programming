#!/usr/bin/python3
""" module contains: class Rectangle """


class Rectangle:
    """
        Rectangle: defines a rectangle
        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
        Method:
            __init__: Initializer of the width and height for instances of the rectangle height and width
    """

    def __init__(self, width=0, height=0):
        """ Initialization of attributes for instances
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        if (isinstance(width, int)):
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
        else:
            raise TypeError('width must be an integer')

        if (isinstance(height, int)):
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        """ getter for width
            Return:
                width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width
            Args:
                value (int): width value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ getter  for the height
            Return:
                The height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function for height
            Args:
                value (int): Then new height value
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
