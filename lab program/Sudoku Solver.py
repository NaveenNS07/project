def solveSudoku(board):
    def isValid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num:
                return False

        for x in range(9):
            if board[x][col] == num:
                return False

        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + startRow][j + startCol] == num:
                    return False

        return True

    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if isValid(board, i, j, num):
                            board[i][j] = num
                            if solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    solve(board)

sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solveSudoku(sudoku_board)
print("Solved Sudoku:")
for row in sudoku_board:
    print(row)
