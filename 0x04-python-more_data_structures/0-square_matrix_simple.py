#!/usr/bin/python3

'''
square_matrix_simple :squares each element in a matrix
@matrix : matrix to square each element
'''


def square_matrix_simple(matrix=[]):
    newMatrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            newMatrix[column][row] = matrix[column][row] ** 2
    return newMatrix
