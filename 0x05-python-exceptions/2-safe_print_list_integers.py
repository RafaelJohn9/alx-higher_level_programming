#!/usr/bin/python3

'''
safe_print_list_integers-prints x elements of a list
@my_list:list where elements will be got from
@x:up to this element
'''


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
            i += 1
        except TypeError:
            i += 1
            continue
        except ValueError:
            i += 1
            continue
    print()
    return count
