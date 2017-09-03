# 1032 / 1032 test cases passed.
# Status: Accepted
# Runtime: 45 ms

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            x = '-' + x[1:][::-1]
        else:
            x = x[::-1]
        x = int(x)
        return 0 if x > 2**31 or x < -2**31 else x
