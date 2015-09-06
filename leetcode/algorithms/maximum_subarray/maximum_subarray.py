class Solution(object):
    def maxSubArray(self, nums):
        total_max = current_max = nums[0]

        for value in nums[1:]:
            current_max = max(value, value + current_max)
            total_max = max(current_max, total_max)

        return total_max
