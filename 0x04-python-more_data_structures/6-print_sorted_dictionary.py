#!/usr/bin/python3

'''
print_sorted_dictionary- a function that prints a dictionary by ordered keys.
@a_dictionary:dictionary to be sorted
Return:sorted a_dictionary
'''


def print_sorted_dictionary(a_dictionary):
    for element in sorted(a_dictionary):
        value = a_dictionary[element]
        print("{}: {}".format(element, value))
