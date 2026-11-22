#!/usr/bin/env python3
# Module for calculating the inverse of a matrix.

def inverse(matrix):
    """Calculate the inverse of a square matrix.

    Pseudocode:
        1. Check that matrix is a list of lists.
        2. Check that matrix is non-empty and square.
        3. Calculate the determinant of the matrix.
        4. If the determinant is zero, return None.
        5. Calculate the cofactor matrix.
        6. Transpose the cofactor matrix to get the adjugate.
        7. Divide every element of the adjugate by the determinant.
        8. Return the resulting inverse matrix.

    Args:
        matrix (list): A square matrix represented by a list of lists.

    Returns:
        list or None: The inverse matrix, or None if singular.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is empty or not square.
    """
    if (not isinstance(matrix, list) or not matrix
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    def determinant(mat):
        """Calculate the determinant of a matrix.

        Args:
            mat (list): A square matrix.

        Returns:
            int or float: The determinant.
        """
        size = len(mat)

        if size == 1:
            return mat[0][0]

        if size == 2:
            return (mat[0][0] * mat[1][1]
                    - mat[0][1] * mat[1][0])

        det = 0

        for col in range(size):
            submatrix = [
                row[:col] + row[col + 1:]
                for row in mat[1:]
            ]
            det += ((-1) ** col * mat[0][col]
                    * determinant(submatrix))

        return det

    det = determinant(matrix)

    if det == 0:
        return None

    if n == 1:
        return [[1 / det]]

    cofactor_matrix = []

    for i in range(n):
        row_cofactors = []

        for j in range(n):
            submatrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix)
                if k != i
            ]

            value = ((-1) ** (i + j)
                     * determinant(submatrix))

            row_cofactors.append(value)

        cofactor_matrix.append(row_cofactors)

    adjugate_matrix = [
        list(row) for row in zip(*cofactor_matrix)
    ]

    inverse_matrix = [
        [element / det for element in row]
        for row in adjugate_matrix
    ]

    return inverse_matrix
