# 136 / 136 test cases passed.
# Status: Accepted
# Runtime: 39 ms

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for m in matrix:
        #     if target in m:
        #         return True
        # return False
        if not matrix or not matrix[0]:
            return False
        row = -1
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = left + (right - left)/2
            if matrix[mid][0] == target:
                row = mid
                break
            if matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid + 1
        if row == -1: row = right
        if row == -1: return False
        # python optimized search fun in list
        return target in matrix[row]
