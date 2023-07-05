#!/usr/bin/python3
"""This module solve N queen puzzle"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """
    Solve the N-Queens problem recursively using backtracking.

    Args:
        board (list): The chessboard.
        col (int): The current column to place a queen.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    N = len(board)

    # Base case: All queens are placed
    if col >= N:
        print_solution(board)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0

    return False


def print_solution(board):
    """
    Print a solution to the N-Queens problem.

    Args:
        board (list): The chessboard.
    """
    N = len(board)
    solution = []

    for i in range(n):
        row = ""
        for j in range(n):
            if board[i][j] == 1:
                row += "Q "
            else:
                row += ". "
        solution.append(row.strip())

    print("\n".join(solution))
    print()


def nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Args:
        n (int): The board size.

    Returns:
        int: The exit status.
    """
    # Check if n is an integer
    if not isinstance(n, int):
        print("N must be a number")
        return 1

    # Check if n is at least 4
    if n < 4:
        print("N must be at least 4")
        return 1

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0)

    return 0


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the board size from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Solve the N-Queens problem
    sys.exit(nqueens(N))
