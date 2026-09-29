class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack(num_l, num_r):
            if len(path) == n * 2:
                res.append("".join(path))
                return
            
            if num_l > 0:
                path.append("(")
                backtrack(num_l - 1, num_r + 1)
                path.pop()
            if num_r > 0:
                path.append(")")
                backtrack(num_l, num_r - 1)
                path.pop()
        
        backtrack(n, 0)
        return res