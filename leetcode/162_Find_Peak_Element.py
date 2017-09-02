# 58 / 58 test cases passed.
# Status: Accepted
# Runtime: 39 ms

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(nums):
            if i and i < len(nums) - 1:
                if n > nums[i-1] and n > nums[i+1]:
                    return i
        else:
            return 0 if len(nums) == 1 or nums[0] > nums[1] else len(nums) - 1
