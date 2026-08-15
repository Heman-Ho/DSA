class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 1. Search for the node in the BST
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Node found! Handle the 3 deletion cases:

            # Case A: No left child (0 or 1 child) -> replace with right child
            if not root.left:
                return root.right

            # Case B: No right child (1 child) -> replace with left child
            if not root.right:
                return root.left

            # Case C: Two children -> find In-Order Successor (min in right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left

            # Copy successor's value to current node
            root.val = curr.val

            # Recursively delete the successor from the right subtree
            root.right = self.deleteNode(root.right, curr.val)

        return root