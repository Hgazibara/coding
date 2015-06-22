import numpy as np

expected_set = set(xrange(1, 10))

def validSolution(board):
    board = np.array(board)
    assert board.shape == (9, 9)

    # check rows and columns
    for i in xrange(9):
        if set(board[i]) != expected_set:
            return False
        if set(board[:, i]) != expected_set:
            return False

    # check sub-groups
    for i in xrange(0, 8, 3):
        if set(board[i : i+3, i : i+3].flatten()) != expected_set:
            return False

    return True
