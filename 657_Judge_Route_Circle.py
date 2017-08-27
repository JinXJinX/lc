# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 39 ms

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
