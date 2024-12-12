#!/usr/bin/python3
"""Prime Game - Maria and Ben are playing a game"""


def prime_game(rounds, nums):
    """Determine the winner of multiple rounds of the prime game.

    Args:
        rounds (int): The number of rounds.
        nums (list): List of integers for each round.

    Returns:
        str: The name of the player who won the most rounds ('Maria' or 'Ben').
              If there is no winner, returns None.
    """
    if rounds <= 0 or nums is None:
        return None
    if rounds != len(nums):
        return None

    player_ben = 0
    player_maria = 0

    # Create a list to mark prime numbers using Sieve of Eratosthenes
    max_number = sorted(nums)[-1]
    sieve = [1 for _ in range(max_number + 1)]
    sieve[0], sieve[1] = 0, 0  # 0 and 1 are not prime

    # Mark multiples of primes as 0
    for i in range(2, len(sieve)):
        if sieve[i] == 1:  # i is prime
            remove_multiples(sieve, i)

    # Count the number of wins for each player based on the rounds
    for n in nums:
        prime_count = sum(sieve[:n + 1])
        if prime_count % 2 == 0:
            player_ben += 1
        else:
            player_maria += 1

    # Determine the overall winner
    if player_ben > player_maria:
        return "Ben"
    if player_maria > player_ben:
        return "Maria"
    return None


def remove_multiples(sieve_list, prime):
    """Removes multiples of a prime number from the list.

    Args:
        sieve_list (list): List of integers where prime multiples.
        prime (int): The prime number whose multiples will be removed.
    """
    for i in range(2, len(sieve_list)):
        if i * prime < len(sieve_list):
            sieve_list[i * prime] = 0
