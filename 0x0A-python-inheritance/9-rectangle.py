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
        """ attributes of a rectangle 
        with some validation being checked
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ gives area of rectangle"""
        return self.__width * self.__height

    def __repr__(self):
        """ returns rep of the rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height}")


    def __str__(self):
        """ prints out rep of the rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height}")
