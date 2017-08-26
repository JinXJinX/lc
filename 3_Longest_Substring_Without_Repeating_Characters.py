# 983 / 983 test cases passed.
# Status: Accepted
# Runtime: 125 ms

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l, r = 0, 1
        rst = 1
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
            else:
                rst = max(rst, r- l + 1)
                r += 1
        return rst
