
# leetcode-weekly-contest-51
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        val = []
        for o in ops:
            if o == '+':
                val.append(val[-1] + val[-2])
            elif o == 'D':
                val.append(val[-1] * 2)
            elif o == 'C':
                val.pop()
            else:
                val.append(int(o))
        return sum(val)
