def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col

    return None


def is_valid(board, row, col, number):
    # Check row
    for i in range(9):
        if board[row][i] == number:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == number:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number:
                return False

    return True


def solve(board):
    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for number in range(1, 10):
        if is_valid(board, row, col, number):
            board[row][col] = number

            if solve(board):
                return True

            board[row][col] = 0

    return False


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku:")
print_board(board)

if solve(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists.")
