class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return
            grid[r][c] = 0
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for nr, nc in neighbors:
                dfs(nr, nc)
        
        # dfs on every boundary cell, marking connecting island with 0
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        # count how many 1s are left
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += 1
        return res