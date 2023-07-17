#!/usr/bin/python3


"""
square a subclass of Recangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this class deals in with a square; a subclass of rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        square inherits all attributes of rectangle and its error handlers
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size width/height of a square
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        size setter
        """

        self.width = value
        self.height = self.width

    def update(self, *args, **kwargs):
        """
        args provides no keyword argument - order matters
        kwargs provides keyword argument - order does not matter
        """

        attr = ["id", "size", "x", "y"]
        i = 0
        if args is not None and len(args) > 0:
            for value in args:
                setattr(self, attr[i], value)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ 
        returns the attributes of a square
        """
        return {"id":self.id,
                "size":self.width,
                "x":self.x,
                "y":self.y
                }

    def __str__(self):
        """
        string rep when printed out
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
