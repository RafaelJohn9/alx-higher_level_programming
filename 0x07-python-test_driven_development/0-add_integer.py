#!/usr/bin/python3
'''
add_integer-this module adds integer nums
@a:first num
@b:secom
Return:results of addition
'''
def add_integer(a, b=98):
    if not isinstance(a, (int, float)): 
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
