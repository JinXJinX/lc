# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 52 ms
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        for num in nums:
            rst ^= num
        return rst
