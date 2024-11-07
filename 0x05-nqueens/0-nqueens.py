#!/usr/bin/python3
"""N Queens puzzle solver that finds all solutions."""
import sys


def print_solution(board):
    """Print the board in the required format."""
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


def solve_nqueens(board, row, n):
    """Recursive backtracking function to solve the N Queens problem."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # backtrack


def main():
    """Main function to handle input and initiate the solution process."""
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
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
