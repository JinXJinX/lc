# 41 / 41 test cases passed.
# Status: Accepted
# Runtime: 115 ms

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        count = 0
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                rst = max(rst, count)
        return rst
