# 12 / 12 test cases passed.
# Status: Accepted
# Runtime: 76 ms

import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.que = collections.deque(maxlen=size)
        self.size = size
        self.s = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        que = self.que
        if len(que) == self.size:
            self.s -= que.popleft()
        que.append(val)
        self.s += val
        return float(self.s) / len(que)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
