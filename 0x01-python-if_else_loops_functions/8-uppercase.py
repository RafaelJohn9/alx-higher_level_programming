#!/usr/bin/python3

# Changes lowercase to uppercase
def uppercase(str):
    output = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            output += "{}".format(chr(ord(char) - 32))
        else:
            output += "{}".format(char)
    print(output)
