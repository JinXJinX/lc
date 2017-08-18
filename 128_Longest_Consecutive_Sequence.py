# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 42 ms

# since 'i in set' and 'set.remove(x)' takes avg o(1) time.
# thie solution is O(n) time complexity
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        rst = 0
        while nums:
            last = first = nums.pop()
            while first + 1 in nums:
                first += 1
                nums.remove(first)
            while last - 1 in nums:
                last -= 1
                nums.remove(last)
            rst = max(rst, first - last + 1)
        return rst
