from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # do a level order traversal using a queue 
        if not root:
            return None
            
        q = deque()
        q.append(root)

        # for each level traverse backwards on the queue and update next pointer
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            node_next = None
            for i in range(len(q) - 1, -1, -1):
                q[i].next = node_next
                node_next = q[i]
            
        return root
