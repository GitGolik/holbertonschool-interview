#!/usr/bin/python3

def island_perimeter(grid):

    perimeter = 0
    rows = len(grid)
    if rows > 0:
        cols = len(grid[0])
    else :
        cols = 0

    for i in rang(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
