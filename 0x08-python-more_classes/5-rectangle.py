#!/usr/bin/python3
"""
    3-rectangle: class Rectangle
"""


class Rectangle:
    """
        class Rectangle definition of a rectangle
        Attributes:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
            initialises the instances of the class
            Args:
                width (int): The width of the rectangle
                height (int): The height of the rectangle
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
            getter function for the private attribute width
            Retruns: The width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for the private attribute width
            Args:
                value (int): The new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for the private attribute height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the private attribute height
            Args:
                value (int): new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            public instance method for the calculaion of the area of the rectangle
            Returns: area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            public instance method to calculate the perimeter of the rectangle
            Returns: perimeter of the rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            return the string representation of the rectangle
        """
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width

        return rectangle

    def __repr__(self):
        """
            returns string representation of the rectangle
            representation able to be recreated into a new instance
            using eval method
        """
        rectangle = ''
        if self.__width is 0 or self.__height is 0:
            return rectangle
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """
            prints Bye rectangle... when an instance is
            deleted
        """
        print('Bye rectangle...')
