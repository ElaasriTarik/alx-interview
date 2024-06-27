#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """island perimeter function"""

    max_len = len(grid[0])
    perimeter = 0
    grid_len = len(grid)
    for arr in range(grid_len):
        for i in range(0, max_len):
            # check first and last lands
            if grid[arr][i] == 1:
                
                # check first cell or the prev
                if i == 0 or grid[arr][i - 1] == 0:
                    perimeter += 1
                # check last row or next row land
                if arr == grid_len - 1 or grid[arr + 1][i] == 0:
                    perimeter += 1
                # chcek last cell or next land
                if i == max_len - 1 or grid[arr][i + 1] == 0:
                    perimeter += 1
                # check first row or prev row land
                if arr == 0 or grid[arr - 1][i] == 0:
                    perimeter += 1

    return perimeter
