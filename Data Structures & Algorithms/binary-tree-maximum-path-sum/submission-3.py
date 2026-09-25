# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def traverse(node):
            nonlocal res

            if not node:
                return 0
            
            left_gain = max(0, traverse(node.left))
            right_gain = max(0, traverse(node.right))
            
            res = max(res, left_gain + node.val + right_gain)
            return node.val + max(left_gain, right_gain)

        traverse(root)
        return res