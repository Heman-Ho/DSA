class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1:
                    continue
                grid[r][c] = 1
                for dr, dc in directions:
                    stack.append((r + dr, c + dc))
        
        # Run dfs on each island touching the edge of grid replace with 0s
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # run dfs on remaining island to count them
        res = 0
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    res += 1

        return res