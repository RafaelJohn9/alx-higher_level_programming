#!/usr/bin/python3

import sys
'''
safe_function:safely prints out an integer
@value: value to be printed
Return: boolean
'''


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
