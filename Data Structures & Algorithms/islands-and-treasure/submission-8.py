from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        INF = 2**31 - 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = 0

        while q:
            distance += 1
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                for x, y in directions:
                    nr, nc = r + y, c + x
                    if (
                        nr >= ROWS or nr < 0 or
                        nc >= COLS or nc < 0 or
                        grid[nr][nc] == -1 or 
                        grid[nr][nc] != INF # already found shortest distance to this grid space
                    ):
                        continue
                    grid[nr][nc] = distance
                    q.append((nr, nc))
                    


