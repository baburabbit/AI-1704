def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    # If all queens are placed, return True
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_queens(board, col + 1):
                return True

            # If placing the queen in the current position doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no row is found where the queen can be placed in this column, return False
    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def solve_8_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]

    if solve_queens(board, 0):
        print("Solution found:")
        print_solution(board)
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_8_queens()

