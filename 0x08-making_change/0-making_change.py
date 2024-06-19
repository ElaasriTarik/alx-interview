#!/usr/bin/python3


"[1, 2, 25], 50"
"[1256, 54, 48, 16, 102], 1453"
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
