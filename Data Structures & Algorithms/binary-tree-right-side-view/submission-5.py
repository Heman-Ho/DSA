# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            for _ in range(qLen - 1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            right_node = q.popleft()
            res.append(right_node.val)
            if right_node.left:
                q.append(right_node.left)
            if right_node.right:
                q.append(right_node.right)
        return res