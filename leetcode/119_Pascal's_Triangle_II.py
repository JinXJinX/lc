# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 32 ms
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.helper([1], 0, rowIndex)

    def helper(self, lst, curIndex, index):
        if curIndex == index:
            return lst
        new = [1]*(len(lst)+1)
        for i in range(1, len(lst)):
            new[i] = lst[i-1] + lst[i]
        return self.helper(new, curIndex+1, index)
