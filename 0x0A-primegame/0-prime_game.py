#!/usr/bin/python3

"""
Prime Game: Determine the winner of multiple rounds of the game
"""

def is_prime_sieve(max_n):
    """Generate a boolean array indicating primality of numbers up to max_n."""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """
    Determine who the winner is after x rounds of the prime game.
    
    Args:
        x (int): Number of rounds.
        nums (list): Array of n values for each round.
        
    Returns:
        str: Name of the winner ("Maria" or "Ben") or None if a tie.
    """
    if not nums or x <= 0:
        return None

    # Precompute primes up to the maximum number in nums
    max_n = max(nums)
    is_prime = is_prime_sieve(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
