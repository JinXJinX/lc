# 1481 / 1481 test cases passed.
# Status: Accepted
# Runtime: 56 ms

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except ValueError:
            return False
