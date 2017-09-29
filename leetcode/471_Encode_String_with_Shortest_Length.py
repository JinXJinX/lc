class Solution(object):
    def encode(self, s, check={}):
        """
        :type s: str
        :rtype: str
        """
        if s not in check:
            n = len(s)
            i = (s+s).find(s, 1)
            one = '%d[%s]' % (n // i, self.encode(s[:i])) if i < n else s
            mut = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1,n)]
            check[s] = min([s, one] + mut, key=len)
        return check[s]
