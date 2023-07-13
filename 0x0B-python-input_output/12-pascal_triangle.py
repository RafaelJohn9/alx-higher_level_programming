#!/usr/bin/python3

"""
pascalTriangle-it prints a pascal triangle until to the n'th row
"""


def pascal_triangle(n):
    """
    this is a pascal triangle in code
    where n is the row to be reached
    """

    if n <= 0:
        return ([])

    i = 0

    pascalList = []
    previousList = []
    while i < n:
        currentList = []
        currentList.append(1)
        if i == 0:
            pascalList.append(currentList)
            previousList == currentList
            i += 1
            continue
        elif i == 1:
            currentList.append(1)
            pascalList.append(currentList)
            previousList = currentList
            i += 1
            continue
        else:
            index = 0
            while (index + 1 < len(previousList)):
                currentList.append(previousList[index] + previousList[index+1])
                index += 1
            currentList.append(1)
            pascalList.append(currentList)
            previousList = currentList
            index += 1
        i += 1
    return (pascalList)
