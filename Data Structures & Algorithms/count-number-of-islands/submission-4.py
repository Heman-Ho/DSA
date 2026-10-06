class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        0 0 0 0 0 0 
        0 0 0 0 0 0 
        0 0 0 0 0 0

        O(n) time
        O(n) space
        n = size of the grid
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        # dfs: O(N) -> n size of grid 
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for nr, nc in neighbors:
                dfs(nr, nc)
        

        # loop through each cell of the grid
        # if it is an island, run a dfs on that island, and mark all of it's connected land as "0" and increment counter
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        
        return res
                
       
        
