# 110 / 110 test cases passed.
# Status: Accepted
# Runtime: 48 ms
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # because the input nums is sorted. the function is second degree polynomial,
        # so, after applied function, the pos nums and neg nums are still sorted (0
        # is special). So, the timsort, gonna takes O(n) time to sort those two sorted
        # list.
        return [n*(a*n+b)+c for n in nums].sort()
