from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # mark one island with as 2s, 
        # run multi-source bfs on island marked with 1s
        ROWS = len(grid)
        COLS = len(grid[0])
        marked = False

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    marked = True
                    break
            if marked:
                break
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        print(f"intermediate grid: {grid}")
        print(f"initial q: {q}")
        
        res = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for nr, nc in neighbors:
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 2:
                        continue
                    if grid[nr][nc] == 1:
                        return res
                    q.append((nr, nc))
                    grid[nr][nc] = 2
            res += 1