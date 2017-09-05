# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 32 ms

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        level = {0:0}
        rst = 0
        for i, l in enumerate(input.split('\n')):
            w = l.lstrip('\t')
            n = len(l) - len(w)
            if '.' in w:
                rst = max(rst, level[n] + len(w))
            else:
                level[n+1] = level[n] + len(w) + 1
        return rst
