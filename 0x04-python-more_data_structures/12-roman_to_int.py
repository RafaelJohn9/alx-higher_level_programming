#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or len(roman_string) == 0:
        return 0
    key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in roman_string:
        if c not in key:
            return 0
        curr = key[c]
        if curr > prev:
            total += curr - 2 * prev
        else:
            total += curr
        prev = curr
    return total
