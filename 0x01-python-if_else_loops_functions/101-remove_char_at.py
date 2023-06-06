#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    str_1 = "" 

    if (n < 0):
        n = (len(str)) - n

    while i != len(str):
        if (i == n):
            i += 1
            continue
        str_1 += str[i]
        i += 1
    return (str_1)
