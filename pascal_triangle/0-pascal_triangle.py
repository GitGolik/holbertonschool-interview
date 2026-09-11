#!/usr/bin/python3
"""Module containing the creation of pascal triangle"""


def pascal_triangle(n):
    """return pascal triangle in form of list of int"""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
