def spiralize(size):
    board = [[0 for j in xrange(size)] for i in xrange(size)]

    direction = 0
    RIGHT, DOWN, LEFT = 0, 1, 2

    top, bottom = 0, size - 1
    left, right = 0, size - 1

    while bottom >= top:
        if direction == RIGHT:
            for col in xrange(left, right + 1):
                board[top][col] = 1
            top += 1
            if top > 2:
                left += 1
        elif direction == DOWN:
            for row in xrange(top, bottom + 1):
                board[row][right] = 1
            right -= 1
            top += 1
        elif direction == LEFT:
            for col in xrange(right, left - 1, - 1):
                board[bottom][col] = 1
            bottom -= 1
            right -= 1
        else:
            for row in xrange(bottom, top - 1, -1):
                board[row][left] = 1
            left += 1
            bottom -= 1
        direction = (direction + 1) % 4

    return board
