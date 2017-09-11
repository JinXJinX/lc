# 54 / 54 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# one liner
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return [c for c in set(t) if s.count(c) != t.count(c)][0]
