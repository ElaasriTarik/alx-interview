#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """island perimeter function"""

    max_len = len(grid[0])
    perimeter = 0

    for arr in range(len(grid)):
        for i in range(0, max_len):
            # check first and last lands
            if grid[arr][i] == 1:
                # Check left edge or left cell is water
                if i == 0 or grid[arr][i - 1] == 0:
                    perimeter += 1
                # Check right edge or right cell is water
                if i == max_len - 1 or grid[arr][i + 1] == 0:
                    perimeter += 1
                # Check top edge or top cell is water
                if arr == 0 or grid[arr - 1][i] == 0:
                    perimeter += 1
                # Check bottom edge or bottom cell is water
                if arr == len(grid) - 1 or grid[arr + 1][i] == 0:
                    perimeter += 1

    return perimeter
