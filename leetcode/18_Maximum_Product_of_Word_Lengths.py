# 174 / 174 test cases passed.
# Status: Accepted
# Runtime: 632 ms
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sets = [set(w) for w in words]

        rst = 0
        for i, s1 in enumerate(sets):
            for j in range(i+1, len(sets)):
                for c in s1:
                    if c in sets[j]:
                        break
                else:
                    rst = max(rst, len(words[i]) * len(words[j]))
        return rst
