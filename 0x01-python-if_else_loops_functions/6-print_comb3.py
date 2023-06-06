#!/usr/bin/python3

# Prints 2 num combinations excluding identical numbers and combinations
for i in range(0, 100):
    for j in range(i + 1, 10):
        if (i == 8 and j == 9):
            print(f"{i}{j}")
        else:
            print(f"{i}{j},", end=(" "))
