#!/usr/bin/python3
"""
N Queens solver - Places N non-attacking queens on an NxN chessboard
Usage: nqueens N
    - N must be an integer >= 4
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    
    Args:
        board: The current board state represented as a list of queen positions
        row: Row to check
        col: Column to check
        n: Size of the board
    
    Returns:
        Boolean indicating if the position is safe
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][1] == col:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row-1, -1, -1),
                   range(col-1, -1, -1)):
        if i >= 0 and j >= 0 and board[i][1] == j:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row-1, -1, -1),
                   range(col+1, n)):
        if i >= 0 and j < n and board[i][1] == j:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions
    
    Args:
        n: Size of the board and number of queens
    """
    def solve_util(board, row):
        # Base case: If all queens are placed, print the solution
        if row == n:
            print(board)
            return

        # Try placing queen in all columns of this row
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][1] = col
                solve_util(board, row + 1)

    # Initialize the board with first column as row numbers
    # and second column as queen positions (to be filled)
    board = [[i, 0] for i in range(n)]
    solve_util(board, 0)


def main():
    """Main function to handle input and start solving"""
    # Check number of arguments
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

    solve_nqueens(n)


if __name__ == "__main__":
    main()
