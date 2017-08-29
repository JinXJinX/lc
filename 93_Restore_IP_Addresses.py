# 147 / 147 test cases passed.
# Status: Accepted
# Runtime: 46 ms

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rst = []
        self.dfs(s,0, '', rst)
        return rst

    def dfs(self, s, idx, path, rst):
        if idx == 4:
            if not s:
                rst.append(path[:-1])
            return #backtracking
        for i in range(1,4):
            num = s[:i]
            if i <= len(s):
                if int(num) <= 255:
                    self.dfs(s[i:], idx+1, path+num+'.', rst)
                if num[0] == '0':
                    break # avoid leading 0
