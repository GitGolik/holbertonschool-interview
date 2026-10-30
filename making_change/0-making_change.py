#!/usr/bin/python3
"""Making change using dynamic programming."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Args:
        coins (list): coin denominations available.
        total (int): target amount.

    Returns:
        int: minimum number of coins, or -1 if impossible.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Remove duplicates and useless coins larger than total
    coins = sorted(set(c for c in coins if 0 < c <= total), reverse=True)
    if not coins:
        return -1

    # dp[i] = minimum number of coins needed to make amount i
    INF = total + 1
    dp = [0] + [INF] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                continue
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != INF else -1
