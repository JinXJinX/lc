# 60 / 60 test cases passed.
# Status: Accepted
# Runtime: 32 ms
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
