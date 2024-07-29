#!/usr/bin/python3
"""
This module provides functionality to handle and print HTTP status code statistics.

Functions:
    handle(signum, frame): Handles a signal and prints statistics.
    print_stats(count=lines_count): Prints the statistics of HTTP status codes.
"""
import sys
import signal


sizes = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }
lines_count = 0


def handle(signum, frame):
    '''handling signal'''

    global lines_count
    lines_count = 10
    print_stats(lines_count)


def print_stats(count=lines_count):
    '''print stats'''

    global lines_count, sizes
    if lines_count == 10:
        print("File size: ", sizes, end="\n")
        for k, v in codes.items():
            print(f"{k}: {v}")
        lines_count = 0


signal.signal(signal.SIGINT, handle)

while True:
    try:
        if lines_count == 10:
            print_stats(lines_count)
        line = sys.stdin.readline()
        line = line.split()
        if len(line) >= 9:
            sizes += int(line[8])
            codes[line[7]] += 1
            lines_count += 1
    except KeyboardInterrupt:
        continue
