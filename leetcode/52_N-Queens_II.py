# 9 / 9 test cases passed.
# Status: Accepted
# Runtime: 59 ms

# return the number of result
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
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
        #return [['.'*i + 'Q' + '.'*(n-i-1)  for i in r] for r in rst]
        return len(rst)
