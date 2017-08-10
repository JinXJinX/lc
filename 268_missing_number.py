# 121 / 121 test cases passed.
# Status: Accepted
# Runtime: 59 ms

#lol..O(1) space, O(n) time.
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums)**2 + len(nums)) / 2 - sum(nums)
