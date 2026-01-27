#!/usr/bin/python3
"""
N-queens puzzle solver using backtracking.
"""
import sys


def solve_nqueens(n):
    """
    Main function to solve the N-queens problem.
    """
    solutions = []
    board = []
    backtrack(0, n, board, solutions)
    for sol in solutions:
        print(sol)


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    """
    for r, c in board:
        # Check column and diagonals
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def backtrack(row, n, board, solutions):
    """
    Recursive backtracking function to find all solutions.
    """
    if row == n:
        solutions.append([list(item) for item in board])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            backtrack(row + 1, n, board, solutions)
            board.pop()  # Backtrack


if __name__ == "__main__":
    # Handle argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Handle N type
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Handle N value
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
