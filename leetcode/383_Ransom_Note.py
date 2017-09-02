

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # 126 / 126 test cases passed.
        # Status: Accepted
        # Runtime: 172 ms
        from collections import Counter
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        for c in rc.keys():
            if c not in mc or mc[c] < rc[c]:
                return False
        return True

        # or one liner
        # 126 / 126 test cases passed.
        # Status: Accepted
        # Runtime: 166 ms
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

        # and the best solution
        # 126 / 126 test cases passed.
        # Status: Accepted
        # Runtime: 56 ms
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
