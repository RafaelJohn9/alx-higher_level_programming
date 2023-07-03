#!/usr/bin/python3

""" this is a class that defines a rectangle """


class Rectangle:
    """ a real definition of Rectangle """
    def __init__(self, width=0, height=0):
        """ initialises rectangle attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ propery width is being initialised as method"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width parameters and what are being checked"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property height is being initialised as a method"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height parameters being passed and set"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
