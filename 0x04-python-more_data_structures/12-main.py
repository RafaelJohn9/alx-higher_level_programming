#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 5
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IXXX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
