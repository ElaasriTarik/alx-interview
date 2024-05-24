#!/usr/bin/python3
"""UTF VALIDATION"""


def validUTF8(data):
    count = 0
    for d in data:
        if not count:
            count = countOne(d)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if countOne(d) != 1:
                return False
    return count == 0


def countOne(num):
        count = 0
        
        for i in range(7, -1, -1):
            #print(bin(num), bin(num << i))
            if num & (1 << i):
                count += 1
            else:
                break
        return count
