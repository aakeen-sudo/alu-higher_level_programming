#!/usr/bin/python3
"""
Module 2-matrix_divided

Defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0 or not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(n / div, 2) for n in row] for row in matrix]

    return new_matrix