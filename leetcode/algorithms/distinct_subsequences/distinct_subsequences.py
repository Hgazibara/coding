class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)

        counts = [[0 for __ in xrange(n + 1)] for __ in xrange(m + 1)]

        for i in xrange(m):
            counts[i][0] = 1

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                counts[i][j] += counts[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    counts[i][j] += counts[i - 1][j - 1]

        return counts[m][n]
