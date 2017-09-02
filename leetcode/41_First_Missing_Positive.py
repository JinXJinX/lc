
# 156 / 156 test cases passed.
# Status: Accepted
# Runtime: 39 ms

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            m = max(nums)
            from collections import Counter
            c = Counter(nums)
            for i in range(1, m+2):
                if c[i] == 0:
                    return i

        return 1
