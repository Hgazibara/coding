GRID_SIZE = 9
CELL_SIZE = 3
EMPTY = 0

def sudoku(puzzle):
    solution = Solution()
    return solution.solveSudoku(puzzle)


class Solution:
    def solveSudoku(self, grid):
        if is_solved(grid) and is_valid(grid):
            return grid

        i, j = get_blank_space(grid)

        if i == -1 and j == -1:
            return False

        possible_values = get_possible_values(grid, i, j)

        for value in possible_values:
            grid[i][j] = value
            if self.solveSudoku(grid):
                return grid
            grid[i][j] = EMPTY

        return False


def get_blank_space(grid):
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == EMPTY:
                return i, j
    return -1, -1


def is_solved(grid):
    for i in xrange(GRID_SIZE):
        for j in xrange(GRID_SIZE):
            if not is_filled(grid, i, j):
                return False
    return True


def is_valid(grid):
    for i in xrange(GRID_SIZE):
        if not is_valid_set(row(grid, i)):
            return False
        if not is_valid_set(column(grid, i)):
            return False

    # check sub-groups
    for i in xrange(0, GRID_SIZE - 1, CELL_SIZE):
        for j in xrange(0, GRID_SIZE - 1, CELL_SIZE):
            if not is_valid_set(subgroup(grid, i, i + CELL_SIZE, j, j + CELL_SIZE)):
                return False

    return True


def is_valid_set(elements):
    freqs = {}

    for element in elements:
        if element != EMPTY:
            freqs[element] = freqs.get(element, 0) + 1

    return all((count <= 1) for count in freqs.values())


def row(grid, n):
    return grid[n]


def column(grid, n):
    return (grid[x][n] for x in xrange(GRID_SIZE))


def subgroup(grid, i, j, k, l):
    return (grid[m][n] for m in xrange(i, j) for n in xrange(k, l))


def get_possible_values(grid, i, j):
    values = set(x for x in range(1, GRID_SIZE + 1))
    visited = set()

    # remove values from row `i` and column `j`
    visited.update(row(grid, i))
    visited.update(column(grid, j))

    # remove values from a subgrid
    top = (i/3) * 3
    bottom = top + 3
    left = (j/3) * 3
    right = left + 3

    visited.update(subgroup(grid, top, bottom, left, right))
    return (x for x in values - visited)


def is_filled(grid, i, j):
    return grid[i][j] != EMPTY
