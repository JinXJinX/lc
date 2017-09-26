# 149 / 149 test cases passed.
# Status: Accepted
# Runtime: 36 ms
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s1 = bin(x)[2:]
        s2 = bin(y)[2:]
        if len(s1) > len(s2):
            s2 = '0'*(len(s1)-len(s2)) + s2
        elif len(s2) > len(s1):
            s1 = '0'*(len(s2)-len(s1)) + s1
        count = 0
        # print(s1,s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count
