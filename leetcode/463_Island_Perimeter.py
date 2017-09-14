# 5833 / 5833 test cases passed.
# Status: Accepted
# Runtime: 206 ms
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rst = 0
        for g in (grid, zip(*grid)):
            for row in g:
                tmp = 0
                for num in row:
                    if num == 1:
                        tmp = 2
                    elif tmp == 2 : #  and num == 0
                        rst += 2
                        tmp = 0
                rst += tmp
        return rst
