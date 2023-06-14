#!/usr/bin/python3

'''
best_score-function that returns a key with the biggest integer value
a_dictionary=the dict to be checked
Returns:key with biggest int
'''

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_key = None
    best_value = 0

    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value

    return best_key
