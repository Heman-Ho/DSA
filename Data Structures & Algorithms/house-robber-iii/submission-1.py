# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Create a mapping of node referece to max robbed to cache calculations
        max_robbed = {}

        def recursive_rob(node, can_rob):
            if not node:
                return 0
            if not can_rob:
                return recursive_rob(node.left, True) + recursive_rob(node.right, True)
            if node in max_robbed:
                return max_robbed[node]
            val = max(node.val + recursive_rob(node.left, False) + recursive_rob(node.right, False), recursive_rob(node.left, True) + recursive_rob(node.right, True))
            max_robbed[node] = val
            return val
    
                
        
        return recursive_rob(root, True)
