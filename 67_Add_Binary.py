# 294 / 294 test cases passed.
# Status: Accepted
# Runtime: 42 ms

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a if a else '0',2) + int(b if b else '0',2))[2:]
