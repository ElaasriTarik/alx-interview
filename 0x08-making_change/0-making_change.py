#!/usr/bin/python3
"""
makeChange function
"""


def makeChange(coins, total):
    if total <= 0:
        return (0)
    res = 0
    x = 0
    coins = sorted(coins, reverse=True)

    while x < len(coins):
        if total - coins[x] >= 0:
            total -= coins[x]
            res += 1
        if total - coins[x] < 0:
            x += 1
            continue
    if total > 0:
        return -1
    return res
