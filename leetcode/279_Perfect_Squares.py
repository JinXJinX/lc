# 586 / 586 test cases passed.
# Status: Accepted
# Runtime: 262 ms
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        check = [1]
        for i in range(2, int(n ** 0.5)+1):
            check.append(i * i)

        # using a list here will get MLE error.
        stack = set()
        stack.add(n)
        level = 0
        while stack:
            level += 1
            new = set()
            for num in stack:
                for c in check:
                    if num == c:
                        return level
                    elif num > c:
                        new.add(num-c)
            stack = new
        return -1
