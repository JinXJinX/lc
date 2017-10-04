class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)
        idx = s.find('1')
        s = s[idx:]
        r = ''.join('1' if c == '0' else '0' for c in s)
        return int(r, 2)
        
