# 9 / 9 test cases passed.
# Status: Accepted
# Runtime: 75 ms
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # list queens is used to keep only one queen at every row/col
        # list xy_dif keeps only one queen at left to right diagonal
        # list xy_sum keeps only one queen at left to left diagonal
        rst = []
        def dfs(queens, left_d, right_d):
            row = len(queens)
            if row == n:
                rst.append(queens)
                return
            for col in range(n):
                if col not in queens and row-col not in left_d and row+col not in right_d:
                    dfs(queens+[col], left_d+[row-col], right_d+[row+col])
        dfs([],[],[])
        return [['.'*i + 'Q' + '.'*(n-i-1)  for i in r] for r in rst]
