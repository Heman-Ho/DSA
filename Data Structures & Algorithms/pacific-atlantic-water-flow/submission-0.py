class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            # Base cases: out of bounds, already visited, or water cannot flow uphill
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                heights[r][c] < prev_height):
                return

            visited.add((r, c))

            # Explore all 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # 1. Start DFS from Pacific (top/left) and Atlantic (bottom/right) borders
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])             # Top border (Pacific)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Bottom border (Atlantic)

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])             # Left border (Pacific)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Right border (Atlantic)

        # 2. Find intersection of cells that reach both oceans
        return list(pac & atl)