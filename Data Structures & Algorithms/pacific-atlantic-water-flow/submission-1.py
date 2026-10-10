class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, is_pac):
            if is_pac:
                if (r, c) in pac:
                    return
                pac.add((r,c))
            else:
                if (r, c) in atl:
                    return
                atl.add((r,c))

            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for nr, nc in neighbors:
                if (
                    nr < 0 or nr >= ROWS or 
                    nc < 0 or nc >= COLS or 
                    heights[nr][nc] < heights[r][c]
                ):
                    continue
                dfs(nr, nc, is_pac)
            
        for c in range(COLS):
            dfs(0, c, True)
            dfs(ROWS-1, c, False)
        for r in range(ROWS):
            dfs(r, 0, True)
            dfs(r, COLS-1, False)
        
        res = [] 
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
        
