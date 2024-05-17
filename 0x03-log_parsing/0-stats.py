#!/usr/bin/python3

import sys
import os, signal


sizes = 0
codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
lines_count = 0

def handle(signum, frame):
    global lines_count
    lines_count = 10
    print_stats()

def print_stats():
    global lines_count, sizes
    if lines_count == 10:
        print("File size: ", sizes, end="\n")
        for k, v in codes.items():
            print(f"{k}: {v}")
        lines_count = 0
        
signal.signal(signal.SIGINT, handle)

while True:
    try:
        line = sys.stdin.readline()
        line = line.split()
        if len(line) >= 9:
            sizes += int(line[8])
            codes[line[7]] += 1
            lines_count += 1
            print_stats()
    except KeyboardInterrupt:
        continue