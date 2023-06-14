#!/usr/bin/python3

'''
simple_delete-a function that deletes a key in a dictionary.
@a_dictinary: a dictionary
'''


def simple_delete(a_dictionary, key=""):
    try:
        a_dictionary.pop(key)
    except KeyError:
        return a_dictionary
    return a_dictionary
