class Solution:

  def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    queue = [root]
    is_odd = False

    while queue:
      if is_odd:
        l, r = 0, len(queue) - 1
        while l < r:
          queue[l].val, queue[r].val = queue[r].val, queue[l].val
          l += 1
          r -= 1

      next_level = []
      for node in queue:
        if node.left:
          next_level.append(node.left)
        if node.right:
          next_level.append(node.right)

      queue = next_level
      is_odd = not is_odd

    return root