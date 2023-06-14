#!/usr/bin/python3

'''
search_replace-searches and replaces
@my_list:initial list
@search:element to be searched
@replace:char to be replaced
Return: always 0
'''


def search_replace(my_list, search, replace):
    new_list = [0]*len(my_list)
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]

    return new_list
