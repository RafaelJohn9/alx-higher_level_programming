#!/usr/bin/python3

'''
max_integer-searches and returns biggest int
my_list:list to be checked
Returns:biggest int
'''


def max_integer(my_list=[]):
    maxValue = 0
    length = len(my_list)
    if length == 0:
        return None

    while length:
        index = length - 1
        if my_list[index] > maxValue:
            maxValue = my_list[index]
        length -= 1
    return maxValue
