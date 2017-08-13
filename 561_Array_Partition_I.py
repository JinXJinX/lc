# 81 / 81 test cases passed.
# Status: Accepted
# Runtime: 169 ms

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(nums)
        return sum(n for i, n in enumerate(tmp) if i % 2 == 0)
