# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 202 ms
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        rst = []
        i = j = 0
        d = 1
        m, n = len(matrix), len(matrix[0])
        for _ in range(m * n):
            # print(i,j)
            rst.append(matrix[i][j])
            i -= d
            j += d
            if i >= m:
                i = m-1
                j += 2
                d = -d
            if j >= n:
                j = n-1
                i += 2
                d = -d
            if i < 0:
                i = 0
                d = -d
            if j<0:
                j=0
                d = -d
        return rst
