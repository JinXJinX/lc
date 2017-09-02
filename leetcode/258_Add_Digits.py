
# 1101 / 1101 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# math
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if not num else (num - 1) % 9 + 1


# 1101 / 1101 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# iteration
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        rst = 0
        while num:
            rst += num % 10
            num /= 10
            #print(rst)
        return self.addDigits(rst)
