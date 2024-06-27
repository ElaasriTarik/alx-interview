#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """island perimeter function"""

    max_len = len(grid[0])
    perimeter = 0

    for arr in range(max_len - 1):
        for i in range(0, max_len):
            # check first and last lands
            if grid[arr][i] == 1:
                if i == 0 or i == max_len:
                    perimeter += 1
                # check next land
                if grid[arr][i + 1] == 0:
                    perimeter += 1
                # check prev land
                if grid[arr][i - 1] == 0:
                    perimeter += 1
                # check the top land
                if grid[arr - 1][i] == 0:
                    perimeter += 1
                # check the bottom land
                if grid[arr + 1][i] == 0:
                    perimeter += 1

    return perimeter
