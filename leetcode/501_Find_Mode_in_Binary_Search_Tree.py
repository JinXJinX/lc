# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 116 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        rst = []
        while stack:
            n = stack.pop()
            if n:
                stack += [n.left, n.right]
                rst += [n.val]

        from collections import Counter
        count = Counter(rst)
        n = max(count.values())
        rst = []
        for item, num in count.items():
            if num == n:
                rst += [item]
        return rst
