#!/usr/bin/python3

'''
uniq_add- adds all unique integers in a list (only once for each integer
my_list- the list to add the unique integers
Return:sum of uniq integers
'''


def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    summation = 0

    for i in range(len(new_list)):
        summation += new_list[i]

    return summation
