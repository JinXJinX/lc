# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 45 ms

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)

# I know there is a binary search way to solve this, and use O(nlogn) time
