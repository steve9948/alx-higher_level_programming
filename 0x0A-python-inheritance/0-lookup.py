#!/usr/bin/python3


"""Returns a list object."""


def lookup(obj):
    """
    Function returning list of available
    Attributes and methods of an object.
    Use dir() to get a list of all attributesand thier methods.
    """

    attr_and_methods = dir(obj)
    return attr_and_methods
