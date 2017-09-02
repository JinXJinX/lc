# 43 / 43 test cases passed.
# Status: Accepted
# Runtime: 45 ms

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])

        rst = [triangle[0][0]]
        for i, lst in enumerate(triangle[1:]):
            tmp = []
            for j in range(len(lst)):
                if j == 0:
                    tmp.append(lst[0] + rst[0])
                elif j == len(lst) - 1:
                    tmp.append(lst[-1] + rst[-1])
                else:
                    tmp.append(min(rst[j], rst[j-1]) + lst[j])
            rst = tmp
        return min(rst)
