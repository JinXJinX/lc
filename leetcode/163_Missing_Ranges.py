# not elegant enough
# 40 / 40 test cases passed.
# Status: Accepted
# Runtime: 35 ms
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [str(lower) +'->' + str(upper)] if lower < upper else [str(lower)]
        rst = []

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 2:
                rst.append(str(nums[i]-1))
            elif diff > 2:
                rst.append(str(nums[i-1]+1) + '->' + str(nums[i]-1))

        if nums[0] != lower:
            if nums[0] > lower+1:
                rst = [str(lower) + '->' + str(nums[0]-1)] + rst
            else:
                rst = [str(lower)] + rst
        if nums[-1] != upper:
            if nums[-1] == upper - 1:
                rst += [str(upper)]
            else:
                rst += [str(nums[-1]+1) + '->' + str(upper) ]
        return rst

# looks better
# 40 / 40 test cases passed.
# Status: Accepted
# Runtime: 38 ms
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        result = []
        nums.append(upper+1)
        pre = lower - 1
        for i in nums:
           if (i == pre + 2):
               result.append(str(i-1))
           elif (i > pre + 2):
               result.append(str(pre + 1) + "->" + str(i -1))
           pre = i
        return result
