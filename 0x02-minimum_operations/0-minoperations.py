#!/usr/bin/python3
import math
"""
Algorithm file
"""


def minOperations(n):

    if n == 1:
        return [1]

    factors = []
    num = 2
    while num**2 <= n:
        if n % num == 0:
            factors.append(num)
            n //= num
        else:
            n += 1
    if n > 1:
        factors.append(n)

    return sum(factors)


def isPrime(p):
    if p < 2:
        return False
    i = 1
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True
