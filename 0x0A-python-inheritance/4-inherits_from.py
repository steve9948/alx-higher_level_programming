#!/usr/bin/python3
'''Only sub class of.'''


def inherits_from(obj, a_class):
    '''
    Function that returns True if the object is an
    Instance of a class that inherited (directly or indirectly)
    From the specified class ; otherwise False.
    '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
