#!/usr/bin/python3
"""module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists of integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by the given number.

    Raises:
        TypeError: If the matrix is not a valid matrix (list of lists of integers/floats),
            or if each row of the matrix does not have the same size.
        TypeError: If the div parameter is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix
