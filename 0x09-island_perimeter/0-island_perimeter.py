#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Check cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check cell to the left
                    perimeter -= 2
    return perimeter
