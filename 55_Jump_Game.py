
# 75 / 75 test cases passed.
# Status: Accepted
# Runtime: 58 ms

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # m is the max length we can reach
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
