class Solution(object):

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = '#'

    def exist(self, board, word):
        if not word:
            return False

        rows, cols = len(board), len(board[0])

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    board[i][j] = self.visited
                    can_find = self.find(board, i, j, word[1:])

                    if can_find:
                        return True

                    board[i][j] = cell

        return False

    def find(self, board, i, j, word):
        if not word:
            return True

        m = len(board)
        n = len(board[0])

        for di, dj in self.moves:
            ni = i + di
            nj = j + dj

            if ni < 0 or ni == m or nj < 0 or nj == n:
                continue

            if board[ni][nj] != word[0] or board[ni][nj] == self.visited:
                continue

            cell = board[ni][nj]
            board[ni][nj] = self.visited

            can_find = self.find(board, ni, nj, word[1:])

            if can_find:
                return True

            board[ni][nj] = cell

        return False
