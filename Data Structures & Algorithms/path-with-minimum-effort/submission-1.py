import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        min_heap = [(0, (0, 0))] # will hold tuples of (effort, node= (r,c))
        efforts = [[float('inf')] * COLS for _ in range(ROWS)]
        efforts[0][0] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Dijkstra's algorithm
        while min_heap:
            effort, node = heapq.heappop(min_heap)
            r, c = node[0], node[1] 
            
            # If the effort of the current path is greater than a previous path, we can skip it
            if effort > efforts[r][c]:
                continue
            
            # add all it's neighbors to the heap
            for x, y in directions:
                nr, nc = r + x, c + y
                if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0: 
                    continue
                new_effort = max(efforts[r][c], abs(heights[r][c] - heights[nr][nc]))
                if new_effort < efforts[nr][nc]:
                    efforts[nr][nc] = new_effort
                    heapq.heappush(min_heap, (new_effort, (nr, nc)))
        return efforts[-1][-1]
