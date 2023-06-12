#!/usr/bin/python3

'''
delete_at- deletes the item at a specific position in a list.
my_list:is just a list
Return: list
'''


def delete_at(my_list=[], idx=0):
    checkingIndex = 0
    index = 0
    if (idx < 0 or idx > len(my_list)):
        return my_list

    for num in my_list:
        if checkingIndex == idx:
            checkingIndex += 1
            continue
        my_list[index] = num
        index += 1
        checkingIndex += 1
    my_list[-1:] = []
    my_list = my_list[:index]
    return my_list
