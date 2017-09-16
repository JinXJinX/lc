# 23 / 23 test cases passed.
# Status: Accepted
# Runtime: 55 ms
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            dic[len(s)] = dic.get(len(s), []) + [s.encode('utf-8')]
        rst = []
        for lst in dic.values():
            if len(lst) == 1 or len(lst[0]) == 1:
                rst.append(lst)
                continue
            tmp = {}
            for s in lst:
                dis = []
                for i in range(1, len(s)):
                    n = ord(s[i]) - ord(s[i-1])
                    if n < 0:
                        n += 26
                    dis.append(n)
                tup = tuple(dis)
                tmp[tup] = tmp.get(tup, []) + [s]
            rst += tmp.values()
        return rst
