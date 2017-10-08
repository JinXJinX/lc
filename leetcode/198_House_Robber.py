# 69 / 69 test cases passed.
# Status: Accepted
# Runtime: 35 ms

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
