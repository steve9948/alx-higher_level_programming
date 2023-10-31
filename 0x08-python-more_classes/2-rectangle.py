#!/usr/bin/python3
""" module contains: class Rectangle """


class Rectangle:
    """
        Rectangle: defines a rectangle
        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
        Method:
            __init__: Initializes width and height for the instances
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
        """ getter function for the width
            Return:
                width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function for the width
            Args:
                value (int): The new width value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ getter function for the height
            Return:
                height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function for the height
            Args:
                value (int): The new height value
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ finds area of rectangle
            Return:
                area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """ finds the perimeter of rectangle
            Return:
                perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
