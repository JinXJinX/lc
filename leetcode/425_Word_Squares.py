
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0])
        dic = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                dic[word[:i]].append(word)

        rst = []
        def helper(lst):
            if len(lst) ==  n:
                rst.append(lst)
                return
            for word in dic[''.join(zip(*lst)[len(lst)])]:
                helper(lst + [word])

        for word in words:
            helper([word])
        return rst
