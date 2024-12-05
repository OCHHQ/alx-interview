#!/usr/bin/python3
"""
N Queens Problem Solver
The N queens puzzle is to place N non-attacking queens on an N×N chessboard.
This solution prints all possible solutions for a given N.
"""
import sys


def is_safe(board, row, col, n):
    """
    Determine if a queen can be placed on board[row][col]

    Args:
        board: List of lists representing the board
        row: Row to check
        col: Column to check
        n: Size of the board

    Returns:
        Boolean: True if safe, False otherwise
    """
    # Check row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursive utility function to solve N Queens problem

    Args:
        board: List of lists representing the board
        col: Current column
        n: Size of the board
        solutions: List to store all solutions
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    """
    Initialize the board and solve N Queens problem

    Args:
        n: Size of the board
    """
    # Initialize empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens_util(board, 0, n, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


def main():
    """
    Main function to handle input and start solving
    """
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
