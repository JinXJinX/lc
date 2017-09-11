# 54 / 54 test cases passed.
# Status: Accepted
# Runtime: 155 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        rst = 0
        stack = [(root, 1)]
        while stack:
            n, c = stack.pop()
            if n.left:
                stack.append((n.left, c+1 if n.left.val == n.val + 1 else 1))
            if n.right:
                stack.append((n.right, c+1 if n.right.val == n.val + 1 else 1))
            rst = max(rst, c)
        return rst
