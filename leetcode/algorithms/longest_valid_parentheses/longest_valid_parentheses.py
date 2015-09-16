class Solution(object):
    def longestValidParentheses(self, s):
        longest_substring_length = 0
        n = len(s)

        lengths = [0] * n

        for i, c in enumerate(s[1:], 1):
            if c == ')':
                if s[i - 1] == '(':
                    lengths[i] = 2
                    if i >= 2:
                        lengths[i] += lengths[i - 2]
                else:
                    length = lengths[i - 1]
                    j = i - length - 1

                    if j < 0 or s[j] != '(':
                        continue

                    lengths[i] = lengths[i - 1] + 2

                    if j > 0:
                        lengths[i] += lengths[j - 1]

            longest_substring_length = max(longest_substring_length, lengths[i])

        return longest_substring_length
