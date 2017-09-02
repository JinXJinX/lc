# 157 / 157 test cases passed.
# Status: Accepted
# Runtime: 155 ms

class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'x'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'x':
                    self.doit(matrix, i, j)
                    matrix[i][j] = 0
        return

    def doit(self, matrix, x, y):
        for i in range(len(matrix[0])):
            if matrix[x][i] != 'x':
                matrix[x][i] = 0
        for j in range(len(matrix)):
            if matrix[j][y] != 'x':
                matrix[j][y] = 0
