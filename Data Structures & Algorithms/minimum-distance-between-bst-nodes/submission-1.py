class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev = None
        min_diff = float('inf')
        node = root

        while stack or node:
            while node:                 # go all the way left
                stack.append(node)
                node = node.left
            node = stack.pop()           # visit
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            node = node.right            # move to right subtree

        return min_diff