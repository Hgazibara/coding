class Solution(object):
    def numDecodings(self, s):
        n = len(s)

        if n == 0 or s == '0':
            return 0

        self.memory = [-1] * n
        return self.ways(s, 0)

    def ways(self, s, start):
        n = len(s)

        if start == n:
            return 1

        if s[start] == '0':
            return 0

        if self.memory[start] != -1:
            return self.memory[start]

        solution = self.ways(s, start + 1)

        if start < n - 1 and  10 <= int(s[start:start+2]) <= 26:
            solution += self.ways(s, start + 2)

        self.memory[start] = solution
        return self.memory[start]
