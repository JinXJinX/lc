# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 32 ms

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # every path has m-1 times move down, and n-1 times move right.
        # so the total move is m+n-2 moves. you need to choose which points
        # to put those m-1 moves, (or n-1 moves). so its m+n-2 choose m-1
        # ( m-1+n-1 )! / ( (m-1)! * (m-1+n-1-(m-1))! )
        # == ( m-1+n-1 )! / ( (m-1)! * (n-1)! )
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)

# or dp
class Solution(object):
    def uniquePaths(self, m, n):
        table = [[0]*n]*m
        for i in range(m):
            table[i][0] = 1
        for i in range(n):
            table[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]
