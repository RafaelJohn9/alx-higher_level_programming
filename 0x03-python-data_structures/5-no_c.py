#!/usr/bin/python3

# removes all C's
def no_c(my_string):
    string = ""
    i = 0
    str_len = len(my_string)
    while i < str_len:
        if my_string[i] == "c" or my_string[i] == "C":
            i += 1
            continue
        string += my_string[i]
        i += 1
    return (string)
