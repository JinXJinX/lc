# 315 / 315 test cases passed.
# Status: Accepted
# Runtime: 88 ms
# slow AC solution
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        s = ''
        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                tmp = i+1
                while tmp < len(abbr) and abbr[tmp].isdigit(): tmp+=1
                n = abbr[i:tmp]
                if n and n[0] == '0':
                    return False
                s += '[a-z]{{{}}}'.format(n)
                i += len(n)
            else:
                s += abbr[i]
                i += 1
        #print(s)
        s = '^' + s + '$'
        import re
        return True if re.match(s, word) else False
