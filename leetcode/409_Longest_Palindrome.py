# 95 / 95 test cases passed.
# Status: Accepted
# Runtime: 49 ms
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        rst = 0
        c = Counter(s)
        hasOdd = False
        for char, num in c.items():
            if num % 2 == 0:
                rst += num
            else:
                hasOdd = True
                rst += num - 1
        return rst + 1 if hasOdd else rst
