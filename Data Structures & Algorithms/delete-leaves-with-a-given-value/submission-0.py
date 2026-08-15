from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node, target):
            if not node:
                return True
            left = dfs(node.left, target)
            right = dfs(node.right, target)
            if left and right and node.val == target: 
                node.val = '#' 
                return True

        def prune_tree(node):
            if not node:
                return
            if node.left and node.left.val != "#":
                prune_tree(node.left)
            else:
                node.left = None
            if node.right and node.right.val != "#":
                prune_tree(node.right)
            else:
                node.right = None

            return 
        
        dfs(root, target)
        dummy = TreeNode(0, root, None)
        prune_tree(dummy)
        return dummy.left
