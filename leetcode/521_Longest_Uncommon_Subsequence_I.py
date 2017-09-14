# 41 / 41 test cases passed.
# Status: Accepted
# Runtime: 32 ms
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # if a equals to b, then no uncommon substring
        # else, a is uncommon substring of b, and b is uncommon substring of
        # a, so, return the longest.
        return -1 if a == b else max(len(a), len(b))
