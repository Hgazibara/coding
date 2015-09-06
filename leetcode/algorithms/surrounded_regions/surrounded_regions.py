import collections

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution(object):
    def solve(self, board):
        rows = len(board)

        if rows == 0:
            return

        cols = len(board[0])

        does_not_leak = find_leakage_points(board)
        print does_not_leak
        return

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'O' and does_not_leak[i][j]:
                    print i, j, cell
                    board[i][j] = 'X'


def find_leakage_points(board):
    rows, cols = len(board), len(board[0])

    does_not_leak = [[True for __ in xrange(cols)] for __ in xrange(rows)]
    queue = collections.deque()

    for i, j, cell in outer_border(board):
        if cell == 'O':
            queue.append((i, j))

    while queue:
        i, j = queue.popleft()

        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            does_not_leak[i][j] = False

        for ni, nj in neighbors(board, i, j):
            if does_not_leak[ni][nj] == False:
                continue

            if does_not_leak[i][j] == False:
                does_not_leak[ni][nj] = False

            queue.append((ni, nj))

    return does_not_leak


def outer_border(board):
    rows, cols = len(board), len(board[0])

    for i in xrange(rows):
        for j in [0, cols - 1]:
            yield i, j, board[i][j]

    for j in xrange(cols):
        for i in [0, rows - 1]:
            yield i, j, board[i][j]


def neighbors(board, i, j):
    X, Y = len(board) - 1, len(board[0]) - 1

    for di, dj in moves:
        ni = i + di
        nj = j + dj
        if 0 <= ni <= X and 0 <= nj <= Y and board[ni][nj] == 'O':
            yield ni, nj
