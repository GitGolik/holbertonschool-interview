#!/usr/bin/python3
"""Solve the N queens puzzle."""


import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed at (row, col)."""
    for prev_row, prev_col in queens:
        if prev_col == col:
            return False
        if abs(prev_row - row) == abs(prev_col - col):
            return False
    return True


def solve(queens, row, n):
    """Print every solution using backtracking."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve(queens, row + 1, n)
            queens.pop()


def main():
    """Handle command-line arguments and start the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve([], 0, n)


if __name__ == "__main__":
    main()