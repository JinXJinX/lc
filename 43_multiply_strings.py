# 311 / 311 test cases passed.
# Status: Accepted
# Runtime: 415 ms

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                res[i+j] += int(c1) * int(c2)
                res[i+j+1] += res[i+j] //10
                res[i+j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join([str(x) for x in res[::-1]])
