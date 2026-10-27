class Solution:

  def leafSimilar(
      self, root1: Optional[TreeNode], root2: Optional[TreeNode]
  ) -> bool:
    stack1 = [root1] if root1 else []
    stack2 = [root2] if root2 else []

    def get_next_leaf(stack: list[TreeNode]) -> Optional[int]:
      while stack:
        node = stack.pop()

        if not node.left and not node.right:
          return node.val

        if node.right:
          stack.append(node.right)
        if node.left:
          stack.append(node.left)

      return None  # No more leaves left in this tree

    while stack1 or stack2:
      leaf1 = get_next_leaf(stack1)
      leaf2 = get_next_leaf(stack2)

      # If one tree ran out of leaves early, or leaf values don't match
      if leaf1 != leaf2:
        return False

    return True