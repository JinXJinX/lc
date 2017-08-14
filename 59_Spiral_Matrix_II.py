# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 52 ms

# add element from inner part to outside
# rotation List
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        lst =[]
        lo = n * n + 1
        while lo > 1:
            lo, hi = lo - len(lst), lo
            lst = [range(lo, hi)] + zip(*lst[::-1])
        return lst
