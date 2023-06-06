#!/usr/bin/python3

# checks for lowercase letters
def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    else:
        return False
