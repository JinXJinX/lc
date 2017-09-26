# 183 / 183 test cases passed.
# Status: Accepted
# Runtime: 138 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return
        val = 0
        val += 0 if not t1 else t1.val
        val += 0 if not t2 else t2.val
        node = TreeNode(val)
        node.left = self.mergeTrees(None if not t1 else t1.left, None if not t2 else t2.left)
        node.right = self.mergeTrees(None if not t1 else t1.right, None if not t2 else t2.right)
        return node
