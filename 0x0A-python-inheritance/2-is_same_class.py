#!/usr/bin/python3

""" checks if object is the an instance of the specified class"""


def is_same_class(obj, a_class):
    """ a function  that returns a boolean
    while checking if obj is  an instance a _ class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
