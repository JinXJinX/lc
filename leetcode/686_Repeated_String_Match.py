# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 58 ms
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) >= len(B):
            if B in A:
                return 1
            if B in A+A:
                return 2
            return -1
        count = B.count(A)
        B = B.replace(A, '')
        if not B:
            return count
        if B in A:
            return count+1
        for i in range(1, len(B)+1):
            if A.endswith(B[:i]) and A.startswith(B[i:]):
                return count + 2
        else:
            return -1
