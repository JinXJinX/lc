# 60 / 60 test cases passed.
# Status: Accepted
# Runtime: 42 ms

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s):
            return s[::-1]
        lst = list(s)
        for i in range(0, len(s), 2 * k):
            lst[i:i+k] = reversed(lst[i:i+k])
        return ''.join(lst)
