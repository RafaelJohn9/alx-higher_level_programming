#!/usr/bin/python3

'''
safe_print-prints x elements of a list
@my_list:list where elements will be got from
@x:up to this element
'''


def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0

    while i < x:
        try:
            print(f"{my_list[i]}", end="")
            count += 1
            i += 1
        except IndexError:
            print()
            return (count)
    print()
    return count
