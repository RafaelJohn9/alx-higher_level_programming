#!/usr/bin/python3

'''
safe_print_divisipn: divides a and b
@a:first num
@b:second num
Return:value of division else
'''


def safe_print_division(a, b):
    try:
        ans = (a / b)
    except ZeroDivisionError:
        ans = None
    finally:
        print("Inside result: {}".format(ans))
        return ans
