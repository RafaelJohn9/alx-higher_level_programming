#!/bin/python3

# takes the ASCII CODE converts them to char
for i in range(97, 123):
    # conditional statement to check for q and e and skips them
    if (i == 101 or i == 113):
        continue
    else:
        print(chr(i), end="")
