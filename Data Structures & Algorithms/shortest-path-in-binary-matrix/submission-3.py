from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        if len(grid) == 1:
            return 1
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        q = deque()
        visited = set()
        visited.add((0,0))
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # start queue with (0,0)
        q.append((0,0))
        
        # while queue
        while q:
            # increment res
            res += 1
            # process n times where n = len(queue)
            qLen = len(q)
            for _ in range(qLen):
                # pop queue
                r, c = q.popleft()
                # for all neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= ROWS or 
                        nc < 0 or nc >= COLS or 
                        grid[nr][nc] != 0 or 
                        (nr, nc) in visited
                    ):
                        continue

                    # if neighbor is grid[-1][-1] then return our calculated path length
                    if nr == ROWS-1 and nc == COLS-1:
                        return res + 1

                    # add neighbor to the queue and to the visited set
                    visited.add((nr, nc))
                    q.append((nr, nc))
        return -1
