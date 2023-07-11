#!/usr/bin/python3

"""
a square class that inherits from Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """ 
    square; a specialised subclass
    """
    def __init__(self, size):
        """ attributes of a rectangle 
        with some validation being checked
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ gives area of rectangle"""
        return self.__size ** 2

    def __repr__(self):
        """ returns rep of the rectangle """
        return (f"[Rectangle] {self.__size}/{self.__size}")


    def __str__(self):
        """ prints out rep of the rectangle """
        return (f"[Rectangle] {self.__size}/{self.__size}")
