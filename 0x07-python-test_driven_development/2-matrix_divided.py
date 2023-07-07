#!/usr/bin/python3
"""module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list):represented as a list of lists of integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:new matrix as a list of Lists of integers/floats
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "div must be a number"
    msg4 = "division by zero"

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg1)
        if len(row) != len(matrix[0]):
            raise TypeError(msg2)

    if not isinstance(div, (int, float)):
        raise TypeError(msg3)

    if div == 0:
        raise ZeroDivisionError(msg4)

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg1)
            divided_element = round(element / div, 2)
            divided_row.append(divided_element)
        divided_matrix.append(divided_row)

    return divided_matrix
