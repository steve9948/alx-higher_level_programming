#!/usr/bin/python3
'''Creates an empty class.'''


class BaseGeometry:
    '''Represent base geometry.'''

    def area(self):
        '''Area of the shape.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Function to validate whatever value is passed.'''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
