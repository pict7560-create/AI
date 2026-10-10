def safe(board, row, col):

    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):

    if row == 8:
        print(board)
        return True

    for col in range(8):

        if safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


board = [-1] * 8

solve(board, 0)
