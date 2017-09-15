# 106 / 106 test cases passed.
# Status: Accepted
# Runtime: 69 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 1
        self.depth(root)
        return self.best - 1

    def depth(self, root):
        if not root: return 0
        ansL = self.depth(root.left)
        ansR = self.depth(root.right)
        self.best = max(self.best, ansL + ansR + 1)
        return 1 + max(ansL, ansR)
