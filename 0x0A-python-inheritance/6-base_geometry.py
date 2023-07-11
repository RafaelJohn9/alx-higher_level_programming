#!/usr/bin/python3

"""
has a public instance that raises an exception
"""


class BaseGeometry:
    """
    this is a class of BaseGeometry
    """
    def __init__(self):
        """ attributes are not yet defined"""
        pass

    def area(self):
        """area of a figure not yet defined"""
        raise Exception("area() is not implemented")
