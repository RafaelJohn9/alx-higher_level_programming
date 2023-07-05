#!/usr/bin/python3

""" matrix_divided: divides all elements in a matrix """


def matrix_divided(matrix, div):
    """ divides elements in a matrix"""
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_list = []
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            ele = round(element / div, 2)
            new_list.append(ele)
        new_matrix.append(new_list)
    return new_matrix
