#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """determine who the winner of the game is."""
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria = 0
    ben = 0
    for i in range(x):
        primeNos = sieve_of_eratosthenes(nums[i])
        if len(primeNos) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    return None


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes
