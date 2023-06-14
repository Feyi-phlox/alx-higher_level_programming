#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = (len(matrix)

    for row in range(len(matrix)):
        new_matrix[row] = list(map(lambda x: x**2, matrix[row]))

    return (new_matrix)
