#!/usr/bin/python3

def print_last_digit(number):
    sign = 1

    # checks if number is 0
    if (number == 0):
        print(number, end="")
        return

    # if last number is less than 0
    if (number < 0):
        sign = -1
        number *= sign

    # last number logic
    last_num = number % 10
    number *= sign
    print(last_num, end="")

    return (last_num)
