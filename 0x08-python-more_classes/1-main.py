#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

try:
    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
    my_rectangle.width = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
    my_rectangle.width = g
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
except Exception as e:
    print(e)
