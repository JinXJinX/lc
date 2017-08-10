# 53 / 53 test cases passed.
# Status: Accepted
# Runtime: 75 ms

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i, n1 in enumerate(nums):
        #     for j, n2 in enumerate(nums):
        #         if i != j and n1 == n2:
        #             return n1

        l, r = 1, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            l, r = (m+1, r) if sum(n <= m for n in nums) <= m else (l, m)
        return r
