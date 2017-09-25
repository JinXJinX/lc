# 13 / 13 test cases passed.
# Status: Accepted
# Runtime: 258 ms
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = ['']
        if n%2 != 0:
            lst = ['1', '0', '8']
            n -= 1
        while n:
            lst = [ l + item + r for item in lst for l, r in [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')][n<=2:]]
            n -= 2
        return lst
