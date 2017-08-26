# 117 / 117 test cases passed.
# Status: Accepted
# Runtime: 35 ms

# a = ['asdasd', 'asdqwe','asdx','asd']
# zip(*a) ->
# ('a', 'a', 'a', 'a')
# ('s', 's', 's', 's')
# ('d', 'd', 'd', 'd')
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
