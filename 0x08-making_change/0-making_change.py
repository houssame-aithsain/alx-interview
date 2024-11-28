#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, return 0 as no coins are needed
    if total <= 0:
        return 0

    # Initialize dp array with a large value (total + 1, which is impossible)
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make total 0
    dp[0] = 0

    # Iterate through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total can't be made
    return dp[total] if dp[total] != float('inf') else -1
