class Solution(object):
    def containsDuplicate(self, nums):
        visited = set()

        for number in nums:
            if number in visited:
                return True
            visited.add(number)

        return False
