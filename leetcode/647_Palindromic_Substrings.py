# 130 / 130 test cases passed.
# Status: Accepted
# Runtime: 182 ms
class Solution(object):
    def countSubstrings(self, S):
        """
        :type s: str
        :rtype: int
        """
        # N = len(S)
        # ans = 0
        # for center in xrange(2*N - 1):
        #     left = center / 2
        #     right = left + center % 2
        #     while left >= 0 and right < N and S[left] == S[right]:
        #         ans += 1
        #         left -= 1
        #         right += 1
        # return ans
        rst = 0
        for i in range(len(S)):
            left = right = i
            while left >= 0 and right < len(S) and S[left] == S[right]:
                rst += 1
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(S) and S[left] == S[right]:
                rst += 1
                left -= 1
                right += 1
        return rst
