
# 66 / 66 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        rst = root.val
        diff = abs(rst - target)
        while stack:
            n = stack.pop()
            tmp = abs(target - n.val)
            if tmp < diff:
                diff = tmp
                rst = n.val
            if n.right:
                stack.insert(0, n.right)
            if n.left:
                stack.insert(0, n.left)
        return rst
