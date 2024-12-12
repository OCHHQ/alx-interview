#!/usr/bin/python3
"""
Prime Game solution - Determining the winner of a prime number removal game.
"""


def sieve_of_eratosthenes(n):
    """
    Generate all prime numbers up to n using Sieve of Eratosthenes.

    Args:
        n (int): Upper limit for generating primes

    Returns:
        list: List of prime numbers up to n
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [num for num in range(n + 1) if is_prime[num]]


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game across multiple rounds.

    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player with most wins, or None if no winner
    """
    if not nums or x <= 0:
        return None

    # Track wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Memoize prime lists to avoid regenerating for the same n
    prime_cache = {}

    for n in nums:
        # Get prime numbers for this round
        if n not in prime_cache:
            prime_cache[n] = sieve_of_eratosthenes(n)

        primes = prime_cache[n]

        # No primes means Ben wins
        if not primes:
            ben_wins += 1
            continue

        # Simulate the game
        current_set = set(range(1, n+1))
        current_player = 0  # 0 for Maria, 1 for Ben

        while True:
            # Find available primes in the current set
            possible_moves = [p for p in primes if p in current_set]

            # No moves possible
            if not possible_moves:
                # Previous player (who couldn't move) loses
                if current_player == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Player picks the smallest prime and removes it and its multiples
            prime_choice = min(possible_moves)
            current_set = {x for x in current_set if x % prime_choice != 0}

            # Switch players
            current_player = 1 - current_player

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
