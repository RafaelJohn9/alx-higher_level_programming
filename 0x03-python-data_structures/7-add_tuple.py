#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lengthTuple_a = len(tuple_a)
    lengthTuple_b = len(tuple_b)

    if lengthTuple_a == 1:
        newtuple_a = tuple_a + (0,)
    elif lengthTuple_a == 0:
        newtuple_a = (0, 0)
    else:
        newtuple_a = tuple_a

    if lengthTuple_b == 1:
        newtuple_b = tuple_b + (0,)
    elif lengthTuple_b == 0:
        newtuple_b = (0, 0)
    else:
        newtuple_b = tuple_b

    firstValue = newtuple_a[0] + newtuple_b[0]
    secondValue = newtuple_a[1] + newtuple_b[1]
    returnTuple = (firstValue, secondValue)

    return returnTuple
