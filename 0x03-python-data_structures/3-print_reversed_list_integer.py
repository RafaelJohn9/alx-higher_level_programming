#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    length = len(my_list)
    idx_max = length - 1
    while idx_max >= 0:
        print("{:d}".format(my_list[idx_max]))
        idx_max -= 1
