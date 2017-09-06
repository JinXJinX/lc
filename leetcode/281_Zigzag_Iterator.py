# 125 / 125 test cases passed.
# Status: Accepted
# Runtime: 72 ms

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lst = []
        l1 = len(v1)
        l2 = len(v2)
        for i in range(min(l1, l2)):
            self.lst.append(v1[i])
            self.lst.append(v2[i])
        if l1 > l2:
            self.lst.extend(v1[l2:])
        else:
            self.lst.extend(v2[l1:])
        self.idx = 0


    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.lst[self.idx - 1]


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.lst)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
