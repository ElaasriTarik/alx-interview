#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """determine who the winner of the game is."""
    maria = 0
    ben = 0
    for turn in range(x):
        prime_num = None
        for number in nums:
            if is_prime(number):
                prime_num = number
                break

        if prime_num is not None:
            nums.remove(prime_num)
            nums = [num for num in nums if num % prime_num != 0 or
                    num == prime_num]
            print('nums: ', nums)
            if turn % 2 == 0:
                ben += 1
            else:
                maria += 1
    return "Maria" if maria > ben else "Ben"


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
