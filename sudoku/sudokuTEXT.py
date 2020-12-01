# This file contains the text version of the game

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


def solve(row=0, col=0):
    global stop, board
    stop = False
    if col == 9:
        col = 0
        row += 1
    if row == 9:
        stop = True
        return

    if board[row][col] == 0:
        for value in range(1, 10):
            if validPlacement(row, col, value):
                board[row][col] = value
                solve(row, col + 1)
        else:
            if not stop:
                board[row][col] = 0
    else:
        solve(row, col + 1)


def validPlacement(row, col, value):
    global board
    if value in board[row]:
        return False

    column = []
    for board_row in board:
        column.append(board_row[col])
    if value in column:
        return False

    cube = []
    row_index = (row // 3) * 3
    col_index = (col // 3) * 3
    for row in range(row_index, row_index + 3):
        for col in range(col_index, col_index + 3):
            cube.append(board[row][col])
    if value in cube:
        return False

    return True


solve()
print(board)
