# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 79 ms

class Solution(object):
    def addBoldTag(self, s, dic):
        """
        :type s: str
        :type dic: List[str]
        :rtype: str
        """
        lst = [False] * len(s)
        for word in dic:
            index = 0
            while True:
                index = s.find(word, index)
                if index == -1:
                    break
                for i in range(index, index+len(word)):
                    lst[i] = True
                index += 1
        #print(lst)
        rst = ''
        for i, c in enumerate(s):
            if lst[i] and (i == 0 or not lst[i-1]):
                rst += '<b>'
            rst += c
            if lst[i] and (i == len(s)-1 or not lst[i+1]):
                rst += '</b>'
        return rst
