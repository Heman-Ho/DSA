from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c))

        res = 0
        while q:
            q_len = len(q)
            water_found = False

            for _ in range(q_len):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 0:
                        continue
                    water_found = True
                    q.append((nr, nc))
                    grid[nr][nc] = 1
            if water_found:
                res += 1
            
        return res if res != 0 else -1