#!/usr/bin/python3
"""Prime Game: determine the winner of each round."""


def isWinner(x, nums):
    """Return the player who wins the most rounds.

    Args:
        x (int): number of rounds
        nums (list): list of maximum integers for each round

    Returns:
        str: "Maria" or "Ben"
        None: if the winner cannot be determined
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    if max_n < 2:
        return None

    # Sieve of Eratosthenes
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Count of primes <= i
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    maria = 0
    ben = 0

    for i in range(x):
        n = nums[i]
        if n < 2:
            ben += 1
        elif prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
