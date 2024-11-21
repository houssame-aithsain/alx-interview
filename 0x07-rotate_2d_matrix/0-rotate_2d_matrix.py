#!/usr/bin/python3
"""
Module for rotating an n x n 2D matrix by 90 degrees clockwise in-place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): The 2D matrix to rotate.

    Returns:
        None: The matrix is modified in-place.
    """
    # Step 1: Transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()
