# 71 / 71 test cases passed.
# Status: Accepted
# Runtime: 33 ms

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = (map(int, v.split('.')) for v in (version1, version2))
        d = len(v1) - len(v2)
        v1 += [0] * -d
        v2 += [0] * d
        for i in range(len(v1)):
            if v1[i] == v2[i]:
                continue
            elif v1[i] > v2[i]:
                return 1
            else:
                return -1
        return 0
