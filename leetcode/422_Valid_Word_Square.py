# 35 / 35 test cases passed.
# Status: Accepted
# Runtime: 76 ms
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i, word in enumerate(words):
            for j, c in enumerate(word):
                # EASP: Easier to ask for forgiveness than permission
                try:
                    if c != words[j][i]:
                        return False
                except:
                    return False
        return True
