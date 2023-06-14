#!/usr/bin/python3

'''
update_dictionary- a function that replaces or adds key/value in a dictionary
@a_dictionary:dictionaries  to be updated
@key:key to be inserted
@value:value to be inserted
'''


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
