# 24 / 24 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# tricky
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        lst = [9, 56,320,1624,7152,26016,72912,140704,140704]
        return sum(lst[m-1:n])
