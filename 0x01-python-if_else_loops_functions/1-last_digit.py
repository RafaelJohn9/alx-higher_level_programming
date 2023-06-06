#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

# last number logic
if (number < 0):
    sign = -1
    number *= sign
last_num = number % 10
number *= sign

# global statements
print("Last digit of", end=(" "))
print(f"{number}", end=(" "))
print(f"is {last_num}", end=(" "))

# program logic on identifying range of last_num
if (last_num == 0):
    print("and is 0")
elif (last_num > 5):
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
