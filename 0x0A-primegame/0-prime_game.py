#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    
    return is_prime

def prime_game(n, primes):
    taken = [False] * (n + 1)
    moves = 0
    
    for p in range(2, n + 1):
        if primes[p] and not taken[p]:
            moves += 1
            for multiple in range(p, n + 1, p):
                taken[multiple] = True
    
    return moves % 2 == 1  # Maria wins if moves are odd, Ben wins if even

def isWinner(x, nums):
    if not nums or x <= 0:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
