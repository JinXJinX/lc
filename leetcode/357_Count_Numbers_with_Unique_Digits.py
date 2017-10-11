9 / 9 test cases passed.
Status: Accepted
Runtime: 39 ms
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [9, 9, 8, 7, 6,5,4,3,2,1]
        rst, pro = 1,1
        for i in range(n if n <10 else 10):
            pro *= lst[i]
            rst += pro
        return rst
