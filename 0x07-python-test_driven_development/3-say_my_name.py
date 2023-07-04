#!/usr/bin/python3

''' prints my name in stdout'''

def say_my_name(first_name, last_name=""):
    fullname = ''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    fullname += first_name
    fullname += " "
    fullname += last_name
    print (f"My name is {fullname}")
