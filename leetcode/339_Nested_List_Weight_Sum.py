# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 43 ms
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # rst = 0
        # for item in nestedList:
        #     if item.isInteger():
        #         rst += item.getInteger() * dep
        #     else:
        #         rst += self.depthSum(item.getList(), dep+1)
        # return rst
        stack = nestedList[:]
        rst = 0
        dep = 1
        while stack:
            next_stack = []
            for item in stack:
                if item.isInteger():
                    rst += item.getInteger() * dep
                else:
                    next_stack.extend(item.getList())
            dep += 1
            stack = next_stack
        return rst
