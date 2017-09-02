# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 32 ms

# 'strip' can be removed. but, use strip before split, might gives a better performence
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])
