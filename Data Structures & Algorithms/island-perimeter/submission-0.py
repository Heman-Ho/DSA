class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if r - 1 < 0 or grid[r-1][c] == 0:
                        res += 1
                    if r + 1 >= ROWS or grid[r+1][c] == 0:
                        res += 1
                    if c + 1 >= COLS or grid[r][c+1] == 0:
                        res += 1
                    if c - 1 < 0 or grid[r][c-1] == 0:
                        res += 1
        return res