#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    max_len = len(grid[0]) - 1
    perimeter = 0

    for arr in range(max_len):
        for i in range(max_len + 1):
            # check first and last lands
            if i == 1 and i == max_len + 1 or i == max_len + 1 and i == 1:
                perimeter += 1
            # check next land
            if grid[arr][i] == 1 and grid[arr][i + 1] == 0:
                perimeter += 1
            # check prev land
            if grid[arr][i] == 1 and grid[arr][i - 1] == 0:
                perimeter += 1
            # check the top land
            if grid[arr][i] == 1 and grid[arr - 1][i] == 0:
                perimeter += 1
            # check the bottom land
            if grid[arr][i] == 1 and grid[arr + 1][i] == 0:
                perimeter += 1

    return perimeter
