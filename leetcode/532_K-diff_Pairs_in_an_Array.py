# 72 / 72 test cases passed.
# Status: Accepted
# Runtime: 52 ms

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0
