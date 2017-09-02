# 1158 / 1158 test cases passed.
# Status: Accepted
# Runtime: 82 ms

# zigzag
# A   G   M
# B F H L N
# C E I K O
# D   J   P
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rst = [''] * numRows
        idx, step =0, 1
        for c in s:
            rst[idx] += c
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(rst)
