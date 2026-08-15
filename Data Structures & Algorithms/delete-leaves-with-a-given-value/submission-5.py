class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 1. Post-order: Process left and right subtrees first
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # 2. If current node has become a leaf and matches target, prune it
        if not root.left and not root.right and root.val == target:
            return None

        # 3. Otherwise, return the current node to its parent
        return root