#!/usr/bin/python3

'''
multiply_by_2:multiplies value by 2
@a_dictionary:dictionary that returns value multiplied by 2
'''


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in zip(a_dictionary.keys(), a_dictionary.values()):
        new_dict[key] = value * 2
    return new_dict
