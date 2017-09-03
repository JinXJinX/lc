# 11507 / 11507 test cases passed.
# Status: Accepted
# Runtime: 192 ms

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev, p = 0, x
        while p:
            rev = rev * 10 + p % 10
            p /= 10
        return rev == x
