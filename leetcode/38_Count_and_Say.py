# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 49 ms

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'

        for i in range(n-1):
            count = 1
            tmp = ''
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    tmp += str(count)
                    tmp += s[index-1]
                    count = 1
            tmp += str(count)
            tmp += str(s[-1])
            s = tmp
        return s
