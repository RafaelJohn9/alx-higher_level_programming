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

    def integer_validator(self, name, value):
        """
        validates an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
