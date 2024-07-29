#!/usr/bin/python3
"""
Script that reads stdin line by line and handles HTTP status code statistics.
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
    """Handles the signal and prints statistics."""
    global lines_count
    print_stats()
    lines_count = 0


def print_stats():
    """Prints the statistics of HTTP status codes."""
    global sizes, codes
    print(f"File size: {sizes}")
    for code, count in codes.items():
        if count > 0:
            print(f"{code}: {count}")


# Register the signal handler
signal.signal(signal.SIGINT, handle)

for line in sys.stdin:
    try:
        line = sys.stdin.readline()
        line = line.split()
        if len(line) >= 9:
            sizes += int(line[8])
            codes[line[7]] += 1
            lines_count += 1
        if lines_count == 10:
            print_stats(lines_count)
    except KeyboardInterrupt:
        continue
