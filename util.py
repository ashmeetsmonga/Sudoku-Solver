def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def valid(board, num, pos):
    # Checking the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking the col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking the 3 X 3 box
    box_x = (pos[1] // 3) * 3
    box_y = (pos[0] // 3) * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num and pos != (i, j):
                return False

    return True