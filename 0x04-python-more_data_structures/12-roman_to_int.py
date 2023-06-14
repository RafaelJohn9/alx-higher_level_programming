#!/usr/bin/python3

def roman_to_int(roman_string):
    key = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev = 0
    for c in roman_string:
        curr = key[c]
        if curr > prev:
            sum += curr - 2 * prev
        else:
            sum += curr
        prev = curr
    return sum
