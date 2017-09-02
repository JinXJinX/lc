# 10 / 10 test cases passed.
# Status: Accepted
# Runtime: 45 ms

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [r+[num] for r in res]
        return res
