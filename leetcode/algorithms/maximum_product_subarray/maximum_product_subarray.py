class Solution(object):
    def maxProduct(self, nums):
        current_min = nums[0]
        current_max = nums[0]
        total_max = nums[0]

        for value in nums[1:]:
            min_here = current_min
            max_here = current_max

            current_max = max(max(max_here * value, min_here * value), value)
            current_min = min(min(max_here * value, min_here * value), value)

            total_max = max(current_max, total_max)

        return total_max
