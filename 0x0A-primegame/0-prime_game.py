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
        return "Maria"
    return "Maria" if maria > ben else "Ben" if ben > maria else None


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos
