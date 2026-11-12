#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): Maximum number for each round.

    Returns:
        str: Name of the player with the most wins.
        None: If the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)

    if max_num < 2:
        return "Ben"

    # Sieve of Eratosthenes
    is_prime = [True] * (max_num + 1)
    is_prime[0] = False

    if max_num >= 1:
        is_prime[1] = False

    i = 2
    while i * i <= max_num:
        if is_prime[i]:
            j = i * i
            while j <= max_num:
                is_prime[j] = False
                j += i
        i += 1

    # prime_count[n] = number of primes less than or equal to n
    prime_count = [0] * (max_num + 1)
    count = 0

    for n in range(max_num + 1):
        if is_prime[n]:
            count += 1
        prime_count[n] = count

    maria_wins = 0
    ben_wins = 0

    for round_number in range(x):
        n = nums[round_number]

        if n < 2:
            ben_wins += 1
        elif prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"

    if ben_wins > maria_wins:
        return "Ben"

    return None
