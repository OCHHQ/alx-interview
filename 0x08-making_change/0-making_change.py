#!/usr/bin/python3
"""
Module to solve the coin change problem with minimum number of coins.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): List of coin denominations
    total (int): Target amount to make change for

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    # Handle base cases
    if total <= 0:
        return 0

    # Create DP table initialized with a large value
    # (total + 1 works as a "infinity" substitute)
    dp = [total + 1] * (total + 1)

    # Base case: 0 coins needed to make 0 amount
    dp[0] = 0

    # Build solution bottom-up
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result, or -1 if no solution found
    return dp[total] if dp[total] != total + 1 else -1
