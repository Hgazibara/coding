class Solution(object):
    def climbStairs(self, n):
        if n <= 1: return 1

        prev, curr = 1, 2

        for i in xrange(2, n):
            prev, curr = curr, prev + curr

        return curr
