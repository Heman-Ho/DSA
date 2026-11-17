class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = [] 

        def backtrack(num_open, num_closed):
            if len(path) == n * 2:
                res.append("".join(path))
                return
            
            if num_open < n:
                path.append("(")
                backtrack(num_open + 1, num_closed)
                path.pop()
            if num_closed < num_open:
                path.append(")")
                backtrack(num_open, num_closed + 1)
                path.pop()
            
        backtrack(0, 0)
        return res