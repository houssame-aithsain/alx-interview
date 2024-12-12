#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determine the winner of multiple rounds of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers for each round.

    Returns:
        str: The name of the player who won the most rounds ('Maria' or 'Ben').
              If there is no winner, returns None.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    # Create a list to mark prime numbers using Sieve of Eratosthenes
    max_num = sorted(nums)[-1]
    a = [1 for _ in range(max_num + 1)]
    a[0], a[1] = 0, 0  # 0 and 1 are not prime

    # Mark multiples of primes as 0
    for i in range(2, len(a)):
        if a[i] == 1:  # i is prime
            rm_multiples(a, i)

    # Count the number of wins for each player based on the rounds
    for n in nums:
        prime_count = sum(a[:n + 1])
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """Removes multiples of a prime number from the list.

    Args:
        ls (list): List of integers where prime multiples.
        x (int): The prime number whose multiples will be removed.
    """
    for i in range(2, len(ls)):
        if i * x < len(ls):
            ls[i * x] = 0
