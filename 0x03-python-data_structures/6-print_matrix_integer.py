#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for items in rows:
            print("{:d}".format(items), end=" " if items != rows[-1] else "")
        print()
