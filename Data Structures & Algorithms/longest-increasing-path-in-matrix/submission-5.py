class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            best = 0
            for nr, nc in neighbors:
                if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0 or matrix[nr][nc] <= matrix[r][c]:
                    continue
                best = max(best, dfs(nr, nc))
            dp[r][c] = 1 + best
            return 1 + best
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
                res = max(res, dp[r][c])
        
        return res
