# 123 / 123 test cases passed.
# Status: Accepted
# Runtime: 132 ms

class Solution:
    def canPlaceFlowers(self, A, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i-1] == 0)
                and (i == len(A)-1 or A[i+1] == 0)):
                    A[i] = 1
                    n -= 1
        return n <= 0
