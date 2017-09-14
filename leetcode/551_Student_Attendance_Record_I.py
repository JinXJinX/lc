# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 48 ms
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not (s.count('A') > 1 or 'LLL' in s)
