#!/usr/bin/python3


"""
a module that contains the subclass Rectangle from base
"""

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        attributes of an object Rectangle
        """

        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must b > 0")

        if not isinstance(y, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        width attribute getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets the value of width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        height attribute getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets the value of width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        x attribute getter
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        sets the value of x of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """
        y attribute getter
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        sets the value of y of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area of the rectangle is calculated
        """
        return (self.__width * self.__height)

    def display(self):
        """
        displays # type of rectangle
        """

        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        shows the rectangle's id number, position (x, y) and dimension (width, height)
        """

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        updates the attributes of the object
        """
        if args is not None and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                "x": self.x,
                "y":self.y,
                "id":self.id,
                "height":self.height,
                "width":self.width
                }
                
