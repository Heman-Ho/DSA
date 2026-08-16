# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGood(node, val):
            if not node:
                return 0
            isGood = 1 if node.val >= val else 0
            val = max(node.val, val)
            return isGood + countGood(node.left, val) + countGood(node.right, val)
        return countGood(root, root.val)