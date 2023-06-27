#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get or set the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ property declared
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Positions the square
        checks condition
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of the square.
           Returns:
           int: The area of the square.
           """
        return self.__size ** 2

    def my_print(self):
        """Prints # according to size
        if size is 0 it prints a newline only
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
