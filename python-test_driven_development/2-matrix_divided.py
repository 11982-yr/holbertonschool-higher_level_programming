#!/usr/bin/python3
"""
Module that defines the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): List of lists of integers/floats.
        div (int or float): Number to divide each element by.

    Returns:
        list: A new matrix with values divided by div
              and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    if (not isinstance(matrix, list) or
            len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            any(len(row) == 0 for row in matrix)):
        raise TypeError(
            "matrix must be a matrix "
            "(list of lists) "
            "of integers/floats"
        )

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) "
                    "of integers/floats"
                )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix "
                "must have the same size"
            )

    if not isinstance(div, (int, float)):
        raise TypeError(
            "div must be a number"
        )

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
