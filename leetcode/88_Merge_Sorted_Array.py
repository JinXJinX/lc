# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 46 ms

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        m -= 1
        n -= 1
        index = len(nums1) - 1
        while index >= 0:
            val = 0
            if m < 0:
                val = nums2[n]
                n -= 1
            elif n < 0:
                val = nums1[m]
                m -= 1
            else:
                if nums1[m] > nums2[n]:
                    val = nums1[index] = nums1[m]
                    m -= 1
                else:
                    val = nums1[index] = nums2[n]
                    n -= 1
            nums1[index] = val
            index -= 1
