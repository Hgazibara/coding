import math
import numpy as np

class Sudoku(object):

    def __init__(self, board):
        self.board = np.array(board)

    def is_valid(self):
        if self.are_dimensions_incorrect():
            return False

        if self.has_incorrect_type():
            return False

        n = int(math.sqrt(self.board.shape[0]))
        N = n**2

        expected_set = set(xrange(1, N + 1))

        # check rows and columns
        for i in xrange(N):
            if set(self.board[i]) != expected_set:
                return False
            if set(self.board[:, i]) != expected_set:
                return False

        # check sub-groups
        for i in xrange(0, N, n):
            if set(self.board[i : i+n, i : i+n].flatten()) != expected_set:
                return False

        return True

    def are_dimensions_incorrect(self):
        shape = self.board.shape

        if len(shape) != 2 or shape[0] != shape[1]:
            return True

        N = shape[0]

        if N != int(math.sqrt(N))**2:
            return True

        return False

    def has_incorrect_type(self):
        return not issubclass(self.board.dtype.type, np.integer)
