# 81 / 81 test cases passed.
# Status: Accepted
# Runtime: 38 ms

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for i, c in enumerate(citations):
            # if current citation number is greater or equal
            # to the size of the rest list, return the size of rest + 1
            if c >= len(citations) - i:
                return len(citations) - i
        return 0
