#!/usr/bin/python3

""" Square - object it is a 2d object """


class Square:
    """ Square - object it is a 2d object """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ Square - object it is a 2d object """
    def area(self):
        return self.__size * self.__size
