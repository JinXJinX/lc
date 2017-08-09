# 85 / 85 test cases passed.
# Status: Accepted
# Runtime: 72 ms

# 'Moving sorted data in bulk is always faster than comparing and moving
# individual data elements, due to modern hardware architecture. Time complexity
#  is the same because merging n sorted arrays of size n is still O(n^2 * log n)
#   in the worst case.' -- o_sharp (leetcode)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lst = []
        for row in matrix:
            lst += row
        return sorted(lst)[k-1]
