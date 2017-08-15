# 168 / 168 test cases passed.
# Status: Accepted
# Runtime: 159 ms

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.helper(candidates, target, 0, [], res)
        return res

    def helper(self, cand, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(cand)):
            self.helper(cand, target - cand[i], i, path+[cand[i]], res)
