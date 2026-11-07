class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = []
        stack = []
        last_visited = None
        cur = root
        
        while cur or stack:
            if cur:
                res.append(f"({cur.val}")
                if not cur.left and cur.right:
                    res.append("()")
                stack.append(cur)
                cur = cur.left
            else:
                top = stack[-1]
                if top.right and last_visited != top.right:
                    cur = top.right
                else:
                    stack.pop()
                    res.append(")")
                    last_visited = top
                    
        return "".join(res)[1:-1]