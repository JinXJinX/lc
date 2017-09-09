
# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 32 ms
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = r'([0-9]+)\[([a-zA-Z]+)\]'
        while True:
            lst =re.findall(r,s)
            if not lst:
                return s
            for n, w in lst:
                s=s.replace(n+'['+w+']', w * int(n))
