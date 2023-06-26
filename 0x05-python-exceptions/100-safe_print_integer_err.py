#!/usr/bin/python3

import sys
'''
safe_print_integer:safely prints out an integer
@value: value to be printed
Return: boolean
'''


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
