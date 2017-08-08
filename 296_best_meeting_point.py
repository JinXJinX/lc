# 57 / 57 test cases passed.
# Status: Accepted
# Runtime: 45 ms

#manhattan distance: distance between two points is the sum of the absolute
#differences of their Cartesian coordinates.
#therefore, the min-total-distance to all points(2-D) is equal to the min-total-
#distance to all points(1-D) on x-axis plus the min-total-distance to all
#points(1-D) on y-axis.
#in 1-D, the min-total-distance point is the median point

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        xs = []
        ys = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    xs.append(i)
                    ys.append(j)
        total = 0
        for os in (xs, sorted(ys)):
            total += sum([abs(x - os[len(os)//2]) for x in os])
        return total
