
#!/usr/bin/env python3
"""Module for calculating the minor matrix."""

def minor(matrix):
    """Calculate the minor matrix of a square matrix.

    Args:
        matrix (list): A list of lists representing a square matrix.

    Returns:
        list: The minor matrix.

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

    determinant = __import__('0-determinant').determinant

    minor_matrix = []

    for i in range(n):
        row_minors = []

        for j in range(n):
            submatrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix)
                if k != i
            ]

            row_minors.append(determinant(submatrix))

        minor_matrix.append(row_minors)

    return minor_matrix
