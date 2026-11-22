
#!/usr/bin/env python3
"""Module for calculating the adjugate matrix."""


def adjugate(matrix):
    """Calculate the adjugate matrix of a square matrix.

    Pseudocode:
        1. Check that matrix is a list of lists.
        2. Check that matrix is non-empty and square.
        3. If the matrix is 1x1, return [[1]].
        4. Calculate the cofactor for each element:
            a. Remove its row and column.
            b. Calculate the determinant of the remaining matrix.
            c. Apply the alternating sign (-1) ** (i + j).
        5. Transpose the cofactor matrix.
        6. Return the resulting adjugate matrix.

    Args:
        matrix (list): A list of lists representing a square matrix.

    Returns:
        list: The adjugate matrix.

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

    def determinant(mat):
        """Calculate the determinant using cofactor expansion.

        Args:
            mat (list): A square matrix.

        Returns:
            int or float: The determinant of the matrix.
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

    return adjugate_matrix
