# 125 / 125 test cases passed.
# Status: Accepted
# Runtime: 1188 ms
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rst = []
        lst = set()
        lst.add(s)
        while lst:
            for x in lst:
                if self.helper(x):
                    rst.append(x)
            if rst:
                break
            new_lst = set()
            for x in lst:
                for i in range(len(x)):
                    tmp = x[:i] + x[i+1:]
                    new_lst.add(tmp)
            lst = new_lst
            #print(lst)
        return list(set(rst)) if rst else ['']

    def helper(self, s):
        import re
        while s:
            if '(' not in s and ')' not in s:
                return True
            if not re.search('\([a-zA-Z]*\)', s):
                return False
            s = re.sub('\([a-zA-Z]*\)', '', s)
        return True
