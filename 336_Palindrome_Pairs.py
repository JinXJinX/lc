# 134 / 134 test cases passed.
# Status: Accepted
# Runtime: 732 ms

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wordict = {}
        res = []

        wordict = { word:i for i, word in enumerate(words)}
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]

                # tmp1 is header, tmp2 is rest
                # is reversed header part is in the dict, and the rest of word is
                # a palindrome, then, add index to result
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
                    res.append([i,wordict[tmp1[::-1]]])

                # j!= 0 is used to avoid duplicate answer. then do the opposite
                # thing of the last loop
                if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
                    res.append([wordict[tmp2[::-1]],i])

        return res
