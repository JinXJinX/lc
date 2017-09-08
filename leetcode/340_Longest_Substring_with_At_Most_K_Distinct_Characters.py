# 142 / 142 test cases passed.
# Status: Accepted
# Runtime: 89 ms

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = {}
        low, rst = 0, 0
        for i, c in enumerate(s):
            # tricky part. dic only store the most last idx of the letter.
            # when the len of dic exceeds the k, del the min idx charactor in
            # the dic. so the new substring is s[idx+1: curridx+1]
            dic[c] = i
            if len(dic) > k:
                low = min(dic.values())
                del dic[s[low]]
                low += 1
            rst = max(i - low + 1, rst)
        return rst
