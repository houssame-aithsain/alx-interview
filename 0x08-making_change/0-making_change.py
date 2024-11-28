#!/usr/bin/python3

""" Function to determine the fewest number of coins needed to meet a total """


def makeChange(coins, total):
    """
    Calculates the minimum number of coins required to make up a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to be made using the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, returns 0.
             If it's impossible to meet the total with the given coins.
    """
    if not coins:
        return -1
    if total <= 0:
        return 0

    c = 0
    coins = sorted(coins, reverse=True)

    for coin in coins:
        while coin <= total:
            total -= coin
            c += 1
        if total == 0:
            return c

    return -1
