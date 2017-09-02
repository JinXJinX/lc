# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 49 ms

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        for i, w in enumerate(lst):
            lst[i] = w[::-1]
        return ' '.join(lst)
