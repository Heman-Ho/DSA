class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c): 
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return 
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            grid[r][c] = "0"
            for nr, nc in neighbors:
                dfs(nr, nc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        
        return res