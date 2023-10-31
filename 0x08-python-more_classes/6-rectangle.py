#!/usr/bin/python3
"""
    3-rectangle: class Rectangle
"""


class Rectangle:
    """
        class Rectangle defines a rectangle
        Attributes:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            number_of_instances (int): The number of the 
                rectangle instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            initialises the instances
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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            getter function of the attribute width
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
            Returns: The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the attribute height
            Args:
                value (int): The new height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            public instance method that calculates the area of a rectangle
            Returns: The area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            public instance method that calculates the perimeter of a rectangle
            Returns: perimeter of rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            return the rectangle`s string representation
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
            returns rectangle`s string representation
            representation recreated into a new instance
            using eval
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
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
