# 169 / 169 test cases passed.
# Status: Accepted
# Runtime: 72 ms


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        rst = []
        for i in sorted(intervals, key=lambda i: i.start):
            if rst and i.start <= rst[-1].end:
                rst[-1].end = max(rst[-1].end, i.end)
            else:
                rst.append(i),
        return rst
