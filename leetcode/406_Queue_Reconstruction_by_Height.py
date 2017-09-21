# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 132 ms

# 1. Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
# 2. For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        for p in people:
            dic[p[0]] = dic.get(p[0], []) + [p[1]]
        rst = []
        for key in sorted(dic.keys(), reverse=True):
            for k in sorted(dic[key]):
                rst.insert(k, [key, k])
        return rst
