# 123 / 123 test cases passed.
# Status: Accepted
# Runtime: 302 ms

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tmp = sum(nums[:k])
        m = tmp
        for i in range(k, len(nums)):
            tmp -= nums[i - k]
            tmp += nums[i]
            m = max(m, tmp)
        return m / k
