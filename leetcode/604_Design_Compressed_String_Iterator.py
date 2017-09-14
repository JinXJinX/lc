# 169 / 169 test cases passed.
# Status: Accepted
# Runtime: 72 ms
class StringIterator(object):
    import re
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.ns = [int(i) for i in re.split('[a-zA-Z]+',compressedString)[1:]]
        self.cs = re.split('[0-9]+', compressedString)[:-1]
        self.idx = 0
        self.curri = 0


    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        rst = self.cs[self.idx]
        self.curri += 1
        if self.curri >= self.ns[self.idx]:
            self.curri = 0
            self.idx += 1
        return rst


    def hasNext(self):
        """
        :rtype: bool
        """
        return False if self.idx >= len(self.ns) else True



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
