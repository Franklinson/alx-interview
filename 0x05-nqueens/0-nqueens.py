#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking
        queens on an N×N chessboard """


import sys


def is_valid(board, row, col):
    """Checks if a queen can be placed at
    the given position without conflicts."""
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return False
        return True


def solve_n_queens(n, board, row):
    """Recursively finds all valid placements of N queens on an NxN board."""
    if row == n:
        # A valid solution has been found, print the board configuration
        for i in range(n):
            print(" " * (n - board[i]) + "Q" + " " * (board[i] - 1))
            print()

    else:
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve_n_queens(n, board, row + 1)


def main():
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

    board = [-1] * n

    solve_n_queens(n, board, 0)


if __name__ == "__main__":
