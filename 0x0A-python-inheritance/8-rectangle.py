#!/usr/bin/python3

"""
a rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle a specialised subclass
    """
    def __init__(self, width, height):
        """
        attributes of a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
