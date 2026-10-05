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
            if node.val >= max_val:
                return 1 + countGood(node.left, node.val) + countGood(node.right, node.val)
            else:
                return countGood(node.left, max_val) + countGood(node.right, max_val)
        
        return countGood(root, root.val)