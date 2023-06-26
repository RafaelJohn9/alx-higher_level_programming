#!/usr/bin/python3

'''
safe_print_integer:safely prints out an integer
@value: value to be printed
Return: boolean
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
