"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
              5
            3   4 
          2   1
        """
        def traverse(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            if left and right:
                return node
            return left or right
            
        return traverse(root)