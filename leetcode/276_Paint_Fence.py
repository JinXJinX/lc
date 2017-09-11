'''
n = 2, there are k * 1 way to painting same color. and k(k-1) way for different
color.
n = 3, if 1st and 2nd fence are same color(k*1), the 3rd one has k-1 posible ways,
if 1st & 2nd are diff, the 3rd has k-1 way for diff color and 1 way for same color
with previous fence. its k * (k-1) or (k*(k-1)) * 1. k(k-1)
previous fences have k + k(k-1) possible combinations. so its (k+k(k-1))*(k-1)
possible ways for 3rd and 2nd has different color.
'''
# 79 / 79 test cases passed.
# Status: Accepted
# Runtime: 35 ms
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        k1 = k-1
        same, diff = k, k*k1
        for i in range(3, n+1):
            same, diff = diff, (same + diff) * k1
        return same + diff
