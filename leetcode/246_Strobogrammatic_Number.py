# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 32 ms

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6",
        }
        res = []
        for d in list(num):
            if d in dic:
                res.append(dic[d])
            else:
                return False
        return list(num) == res[::-1]
