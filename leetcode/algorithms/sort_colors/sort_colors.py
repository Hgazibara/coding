class Solution(object):
    def sortColors(self, nums):
        colors = [0] * 3

        for num in nums:
            colors[num] += 1

        position = 0

        for i in xrange(3):
            for j in xrange(colors[i]):
                nums[position] = i
                position += 1
