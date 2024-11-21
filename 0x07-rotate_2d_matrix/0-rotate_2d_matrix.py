#!/usr/bin/python3
"""
Module for rotating an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): The input square matrix to be rotated.

    Note:
        - The rotation is done in-place
        - No return value is needed as the matrix is modified directly
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        # Reverse the row in-place
        matrix[i].reverse()
