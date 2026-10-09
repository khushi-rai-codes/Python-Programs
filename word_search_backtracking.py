def search_word(board, word):
    rows = len(board)
    cols = len(board[0])

    visited = set()

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (
            row < 0 or
            row >= rows or
            col < 0 or
            col >= cols
        ):
            return False

        if (row, col) in visited:
            return False

        if board[row][col] != word[index]:
            return False

        visited.add((row, col))

        for dr, dc in directions:
            if backtrack(
                row + dr,
                col + dc,
                index + 1
            ):
                return True

        visited.remove((row, col))

        return False

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = input("Enter the word to search: ").upper()

if search_word(board, word):
    print(f"'{word}' exists in the board.")
else:
    print(f"'{word}' does not exist in the board.")
