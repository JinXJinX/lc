# 125 / 125 test cases passed.
# Status: Accepted
# Runtime: 135 ms

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        rst = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                rst = s if abs(s - target) < abs(rst - target) else rst
                if s == target:
                    return s
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return rst
