#!/usr/bin/python3

""" this is a class that defines a rectangle """


class Rectangle:
    """ a real definition of Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes attributes"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
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

    def area(self):
        """ finds the area of object rectangle"""
        return self.__width * self.__height

        self.__width = width
        self.__height = height

        # this is the counting of number of instances
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ finds the area of object rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """finds perimeter of object rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ this is a static method that returns rectangle with biggest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """  output  a str rectangle made of print_symbol"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """  output  a str explaining class input"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ prints out only if an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """ changes rectangle to a square"""
        return cls(size, size)
