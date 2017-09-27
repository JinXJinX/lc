# 102 / 102 test cases passed.
# Status: Accepted
# Runtime: 32 ms
class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # its 10 base number convert to 9 base number
        ans = ''
        while n:
            ans = str(n%9) + ans
            n /= 9
        return int(ans)
