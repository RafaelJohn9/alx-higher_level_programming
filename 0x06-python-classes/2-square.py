#!/usr/bin/python3

""" Square - receives size makes it private atrribute"""



class Square:
    def __init__(self, size=0):
        """ Square - receives size makes it private atrribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
