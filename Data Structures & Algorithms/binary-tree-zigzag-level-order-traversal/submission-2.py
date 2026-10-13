# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        left_to_right = True
        while q:
            qLen = len(q)
            path = [0] * qLen

            for i in range(qLen):
                node = q.popleft()
                path[i] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if left_to_right:
                res.append(path)
            else:
                res.append(reversed(path))

            left_to_right = not left_to_right

        return res