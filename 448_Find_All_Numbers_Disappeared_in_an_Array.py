# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 332 ms

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])

        return [i+1 for i in range(len(nums)) if nums[i] > 0]
