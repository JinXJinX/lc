# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 42 ms
class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.helper(pattern, s, {})

    def helper(self, pattern, s, dic):
        if len(pattern) == 0:
            return True if len(s) == 0 else False
        for end in range(1, len(s)-len(pattern)+2):
            if pattern[0] in dic and dic[pattern[0]] == s[:end]:
                if self.helper(pattern[1:], s[end:], dic):
                    return True
            elif pattern[0] not in dic and s[:end] not in dic.values():
                dic[pattern[0]] = s[:end]
                if self.helper(pattern[1:], s[end:], dic):
                    return True
                del dic[pattern[0]]
        return False
