#!/usr/bin/python3
""" Module for solving prime game question """


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game across multiple rounds.

    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player with most wins, or None if no winner
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    
    # Create Sieve of Eratosthenes
    my_filter = [True] * (max_num + 1)
    my_filter[0] = my_filter[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if my_filter[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, max_num + 1, i):
                my_filter[j] = False

    # Count cumulative primes
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(2, max_num + 1):
        if my_filter[i]:
            count += 1
        prime_count[i] = count

    # Count wins for Maria
    maria_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1

    # Determine overall winner
    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "me"
    return "col"
