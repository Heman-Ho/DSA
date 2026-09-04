class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        ROWS = len(image)
        COLS = len(image[0])
        def dfs(sr, sc, orig_color, target_color):
            if sr < 0 or sr >= ROWS or sc < 0 or sc >= COLS or (sr, sc) in visited or image[sr][sc] != orig_color:
                return
            image[sr][sc] = target_color
            visited.add((sr, sc))
            dfs(sr+1, sc, orig_color, target_color)
            dfs(sr-1, sc, orig_color, target_color)
            dfs(sr, sc+1, orig_color, target_color)
            dfs(sr, sc-1, orig_color, target_color)
            
        dfs(sr, sc, image[sr][sc], color)
        return image