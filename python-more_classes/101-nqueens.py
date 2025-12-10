#!/usr/bin/python3
"""N queens puzzle solver.

Usage:
    nqueens N

N must be an integer greater than or equal to 4.
Only sys is imported.
"""

import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(row, col, cols, diag1, diag2):
    """Check if it's safe to place a queen at (row, col)."""
    if col in cols:
        return False
    if (row + col) in diag1:
        return False
    if (row - col) in diag2:
        return False
    return True


def solve_nqueens(n, row, cols, diag1, diag2, solution, solutions):
    """Use backtracking to find all solutions."""
    if row == n:
        # append solution like [[0, col0], [1, col1], ...]
        solutions.append([[r, solution[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(row, col, cols, diag1, diag2):
            # Place queen
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            solution[row] = col

            # Recurse
            solve_nqueens(n, row + 1, cols, diag1, diag2, solution, solutions)

            # Backtrack
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
            solution[row] = -1


def main():
    """Entry point: parse arguments and solve N queens."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    n_str = sys.argv[1]

    try:
        n = int(n_str)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    cols = set()
    diag1 = set()   # row + col
    diag2 = set()   # row - col
    solution = [-1] * n

    solve_nqueens(n, 0, cols, diag1, diag2, solution, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
