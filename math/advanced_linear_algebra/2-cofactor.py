#!/usr/bin/env python3
#Module for calculating the cofactor matrix.

def cofactor(matrix):
    """Calculate the cofactor matrix of a square matrix.

    Args:
        matrix (list): A list of lists representing a square matrix.

    Returns:
        list: The cofactor matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is empty or not square.
    """
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minor = __import__('1-minor').minor
    minor_matrix = minor(matrix)

    cofactor_matrix = []

    for i in range(n):
        row_cofactors = []

        for j in range(n):
            value = ((-1) ** (i + j)) * minor_matrix[i][j]
            row_cofactors.append(value)

        cofactor_matrix.append(row_cofactors)

    return cofactor_matrix
