#!/usr/bin/python3

"""lookup returns a list of attributes and methods that are in an object"""


def lookup(obj):
    """ returns methods and attributes available in an obect """
    return dir(obj)
