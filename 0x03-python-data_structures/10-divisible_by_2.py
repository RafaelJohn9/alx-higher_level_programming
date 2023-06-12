#!/usr/bin/python3

'''
divisible_by_2-a function that finds all multiples of 2 in a list
my_list:list to be checked
Return: a list with boolean
'''


def divisible_by_2(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    index = 0
    booleans = []
    while index < length:
        if (my_list[index] % 2) == 0:
            booleans.append(True)
            index += 1
        else:
            booleans.append(False)
            index += 1
    return booleans
