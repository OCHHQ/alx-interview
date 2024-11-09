#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in a file that initially contains a single H character.
    Args:
        n (int): The target number of H characters
    Returns:
        int: The minimum number of operations needed.Returns 0
        if n is impossible
        to achieve
    """
    # If n is less than 1, it's impossible to achieve
    if n < 1:
        return 0
    # If n is 1, we already have one H, so no operations needed
    if n == 1:
        return 0
    operations = 0
    divisor = 2
    # Continue until n is fully factorized
    while n > 1:
        # If n is divisible by the current divisor
        while n % divisor == 0:
            # Add the divisor to operations (Copy All + Past)
            operations += divisor
            # Divide n by the divisor
            n //= divisor
        # Move to next potential divisor
        divisor += 1
        # Optimization:squared is greater than n,and n is greater than 1
        # then n is prime.Add n to operations and break
        if divisor * divisor > n and n > 1:
            operations += n
            break
    return operations
