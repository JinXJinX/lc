# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 36 ms

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        rst = []
        return self.helper(k, n, rst, [], 1)

    def helper(self, k, n , rst, lst, idx):
        if len(lst) == k:
            if sum(lst) == n:
                rst.append(lst)
            return

        for i in range(idx, 10):
            if i not in lst:
                self.helper(k, n, rst, lst + [i], i+1)
        return rst
