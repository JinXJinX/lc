# 39 / 39 test cases passed.
# Status: Accepted
# Runtime: 82 ms

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        rst = 0
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i-1]
            if diff >= duration:
                rst += duration
            else:
                rst += diff
        return rst + duration
