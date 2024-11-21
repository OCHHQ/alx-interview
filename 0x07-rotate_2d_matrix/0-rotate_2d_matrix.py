#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D natrix 90 degree clockwise in-place.

    Args:
        matrix(list of lists): n * n 2D natrix to rotate

    Returns:
        None: modifies the matrix in-place
    """
    n = len(matrix)

    # first step here: transpose the matrix
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    #Second step is to reverse each row
    for row in matrix:
        row.reverse()
