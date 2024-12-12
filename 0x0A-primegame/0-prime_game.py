#!/usr/bin/python3


def isWinner(x, nums):
    """
    this function returns the name of the player that won the most rounds
    """
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0], primes[1] = False, False
        for i in range(2, int(limit ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, limit + 1, i):
                    primes[j] = False
        return primes

    def game_round(n):
        primes = sieve_of_eratosthenes(n)
        count = 0
        for i in range(2, n + 1):
            if primes[i]:
                count += 1
        return count % 2 == 1

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if game_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
