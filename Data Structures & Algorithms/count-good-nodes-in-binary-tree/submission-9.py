# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGood(node, max_val):
            if not node:
                return 0
            isGood = 1 if node.val >=  max_val else 0
            max_val = max(node.val, max_val)
            return isGood + countGood(node.left, max_val) + countGood(node.right, max_val)
        return countGood(root, root.val)