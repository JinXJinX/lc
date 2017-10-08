class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lst = [nums[0]] if len(nums) > 0 else []
        for i in range(1, len(nums)):
            self.lst.append(self.lst[-1] + nums[i])
        # print(self.lst)



    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.lst[j] - (self.lst[i-1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
