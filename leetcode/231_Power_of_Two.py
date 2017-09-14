# 1108 / 1108 test cases passed.
# Status: Accepted
# Runtime: 45 ms
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1
