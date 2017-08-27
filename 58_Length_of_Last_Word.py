# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 35 ms

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = s.split()
        return len(lst[-1]) if lst else 0
