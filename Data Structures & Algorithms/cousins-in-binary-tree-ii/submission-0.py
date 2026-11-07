# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        # Queue stores tuples of (node, sum of node and its sibling)
        q = [(root, root.val)]
        
        while q:
            new_q = []
            # Fix: sum the actual node values at the current level, not the stored sibling sums
            total = sum(node.val for node, _ in q)
            
            for node, x in q:
                # Replace the node's value with the cousin sum (total level sum minus node + sibling sum)
                node.val = total - x
                
                # Calculate the sibling sum for the current node's children
                sibling_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                
                if node.left:
                    new_q.append((node.left, sibling_sum))
                if node.right:
                    new_q.append((node.right, sibling_sum))
                    
            q = new_q
            
        return root