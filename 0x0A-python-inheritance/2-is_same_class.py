#!/usr/bin/python3
""" 2-is_same_class: is_same_class """

def is_same_class(obj, a_class):
    '''
    Return true if obj is an instance 
    of the the class else false
    .'''
    if type(obj) == a_class:
        return True
    else:
        return False
