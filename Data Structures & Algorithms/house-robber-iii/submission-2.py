# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def find_max(node, can_rob):
            if not node:
                return 0
            if not can_rob:
                return find_max(node.left, True) + find_max(node.right, True)
            
            return max(
                node.val + find_max(node.left, False) + find_max(node.right, False),
                find_max(node.left, True) + find_max(node.right, True) 
            ) 
        
        return find_max(root, True)
    