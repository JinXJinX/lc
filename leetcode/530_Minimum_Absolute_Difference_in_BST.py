
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this is a brute-force solution. store all nodes vals in a list.
# a better solution should use BST's attribute. the closest vals is the
# largest val on left branch, and smallest val on right branch.
# which is O(1) space, O(nlogn) time
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            nums.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        nums.sort()
        rst = nums[1] - nums[0]
        for i in range(len(nums)-1):
            rst = min(rst, nums[i+1] - nums[i])
        return rst
