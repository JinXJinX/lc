# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 72 ms

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.lst = []
        for v in vec2d:
            self.lst.extend(v)
        self.count = 0


    def next(self):
        """
        :rtype: int
        """
        self.count += 1
        return self.lst[self.count - 1]



    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.lst) > self.count


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
