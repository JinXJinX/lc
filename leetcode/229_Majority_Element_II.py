# 66 / 66 test cases passed.
# Status: Accepted
# Runtime: 62 ms

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        tmp = Counter(nums)
        n = len(nums) // 3
        rst = []
        for v, i in tmp.items():
            if i > n:
                rst.append(v)
        return rst
