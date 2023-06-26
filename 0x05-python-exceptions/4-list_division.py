#!/usr/bin/python3

'''
list_division- a function that divides element by elemeent 2 lists"
@my_list_1: first list
@my_list_2: second list
Return: a new list of length of list_length
'''


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []

    while i < list_length:
        try:
            curr = (my_list_1[i] / my_list_2[i])
            new_list.append(curr)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            i += 1
    return new_list
