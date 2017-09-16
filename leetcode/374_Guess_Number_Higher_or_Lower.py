# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 29 ms

# simple binary search algorithm

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(mid)
            rst = guess(mid)
            if rst > 0:
                lo = mid + 1
            elif rst < 0:
                hi = mid - 1
            else:
                return mid
        return -1
