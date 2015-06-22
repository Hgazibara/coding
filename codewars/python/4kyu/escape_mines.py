import heapq

# (0, 0) is in a top-left corner
# x is a column, y is a row
allowed_moves = (
    ('up', (0, -1)),
    ('down', (0, 1)),
    ('right', (1, 0)),
    ('left', (-1, 0))
)

MAX_X = None
MAX_Y = None

def solve(board, miner, exit):
    global MAX_X, MAX_Y
    MAX_X, MAX_Y = len(board), len(board[0])

    exit = (exit['x'], exit['y'])
    miner = (miner['x'], miner['y'])

    positions = []
    visited_positions = set()

    heapq.heappush(positions, (0, miner, []))

    while positions:
        length, position, moves_made = heapq.heappop(positions)

        if position == exit:
            return moves_made

        visited_positions.add(position)

        for direction, next_position in get_next_positions(position, board):
            if not next_position in visited_positions:
                visited_positions.add(next_position)
                heapq.heappush(positions, (length + 1, next_position, moves_made + [direction]))


def get_next_positions(position, board):
    x, y = position

    for direction, (nx, ny) in allowed_moves:
        next_position = x + nx, y + ny

        if is_allowed(next_position, board):
            yield direction, next_position


def is_allowed(position, board):
    x, y = position
    return 0 <= x < MAX_X and 0 <= y < MAX_Y and board[x][y]
