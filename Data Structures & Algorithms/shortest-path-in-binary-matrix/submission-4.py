from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        q = deque([(0, 0, 1)]) # (r, c, path_length)
        visited = {(0, 0)}

        while q:
            r, c, d = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and not grid[nr][nc] and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
        return -1