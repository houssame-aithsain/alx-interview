#!/usr/bin/python3
"""
Minimum Operations

This script calculates the minimum number of operations required to 
achieve exactly n characters 'H' in a text file by using "Copy All" 
and "Paste" operations.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to get n 'H' characters.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: Minimum number of operations to achieve n 'H' characters or 
         0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Finding factors of n
    while n > 1:
        if n % factor == 0:
            operations += factor  # Copy All and then Paste
            n //= factor
        else:
            factor += 1

    return operations

