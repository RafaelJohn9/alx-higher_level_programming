#!/usr/bin/python3

'''
common_elements- returns a set of common elements in two sets.
@set_1:first set
@set_2:second set
Return: a set
'''


def only_diff_elements(set_1, set_2):
    new_set = set()

    # insert first set
    for element_1 in set_1:
        new_set.add(element_1)

    # inserts second set
    for element_2 in set_2:
        if element_2 in new_set:
            new_set.remove(element_2)
            continue
        new_set.add(element_2)
    return new_set
