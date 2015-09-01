class Solution(object):
    def titleToNumber(self, s):
        column = 0
        power = 1

        for char in reversed(s):
            column += (ord(char) - 65 + 1) * power;
            power *= 26

        return column
