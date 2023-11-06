#!/usr/bin/python3
'''Creates an empty class.'''


class BaseGeometry:
    '''Represent base geometry.'''

    def area(self):
        '''Area of the shape as an exception.'''
        raise Exception("area() is not implemented")
