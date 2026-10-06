def solve_n_queens(n):
    solutions = []

    board = [["."] * n for _ in range(n)]

    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()

    def backtrack(row):
        if row == n:
            solution = ["".join(r) for r in board]
            solutions.append(solution)
            return

        for col in range(n):
            if col in columns:
                continue

            if row + col in positive_diagonals:
                continue

            if row - col in negative_diagonals:
                continue

            board[row][col] = "Q"

            columns.add(col)
            positive_diagonals.add(row + col)
            negative_diagonals.add(row - col)

            backtrack(row + 1)

            board[row][col] = "."

            columns.remove(col)
            positive_diagonals.remove(row + col)
            negative_diagonals.remove(row - col)

    backtrack(0)

    return solutions


n = int(input("Enter the value of N: "))

if n <= 0:
    print("N must be greater than 0.")
else:
    solutions = solve_n_queens(n)

    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}")

    if solutions:
        print("\nFirst solution:")

        for row in solutions[0]:
            print(row)
