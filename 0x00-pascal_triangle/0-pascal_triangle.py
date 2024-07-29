#!/usr/bin/python3
'''pascal triangle module'''


def pascal_triangle(n):
    '''pascal triangle generating function'''
    if n == 0:
      return []

    triangle = []

    for x in range(n):
        triangle.append([])
        triangle[x].append(1)
        if (x > 0):
            for y in range(1, x):
                triangle[x].append(triangle[x - 1][y - 1] + triangle[x - 1][y])
            triangle[x].append(1)
    return (triangle)
