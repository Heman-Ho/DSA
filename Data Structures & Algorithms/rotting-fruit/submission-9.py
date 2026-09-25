from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    num_fresh += 1
        
        mins = 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while num_fresh > 0 and queue:
            qLen = len(queue)
            for i in range(qLen):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    num_fresh -= 1
                    queue.append((nr, nc))
            mins += 1
            
        
        return -1 if num_fresh > 0 else mins
