# 126 / 126 test cases passed.
# Status: Accepted
# Runtime: 119 ms

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if (i % 2) ^ (nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            # the exclusive or operation is used to reduce redundant code.
            # the last two lines equivalent to:
            # if (i % 2 == 1 and num[i] < nums[i-1]) or (i % 2 == 0 and num[i] > nums[i-1]):
            #   nums[i], nums[i - 1] = nums[i - 1], nums[i]
