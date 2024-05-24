#!/usr/bin/python3
"""UTF VALIDATION"""


def validUTF8(data):
    record = 0
    for d in data:
        if not record:
            record = recordOne(d)
            if record == 0:
                continue
            if record == 1 or record > 4:
                return False
            record -= 1
        else:
            record -= 1
            if recordOne(d) != 1:
                return False
    return record == 0


def recordOne(num):
    record = 0

    for i in range(7, -1, -1):
        # print(bin(num), bin(num << i))
        if num & (1 << i):
            record += 1
        else:
            break
    return record
