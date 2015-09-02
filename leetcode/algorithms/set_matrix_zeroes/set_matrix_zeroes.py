class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        positions = [(i, j) for i in xrange(m) for j in xrange(n)]

        for i, j in positions:
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

        for i, j in positions:
            if i in rows or j in cols:
                matrix[i][j] = 0
