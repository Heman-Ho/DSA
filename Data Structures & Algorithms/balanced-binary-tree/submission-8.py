class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # 1. Check left subtree
            left_h = check_height(node.left)
            if left_h == -1:
                return -1  # Early exit: left is already unbalanced

            # 2. Check right subtree
            right_h = check_height(node.right)
            if right_h == -1:
                return -1  # Early exit: right is already unbalanced

            # 3. Check current node
            if abs(left_h - right_h) > 1:
                return -1

            # 4. Return true height
            return 1 + max(left_h, right_h)

        return check_height(root) != -1