#!/usr/bin/python3

"""
a class MyList that inherits from list
"""


class MyList(list):
    """ this is a subclass of list"""

    def print_sorted(self):
        """ prints a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
