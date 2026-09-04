class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        ROWS = len(image)
        COLS = len(image[0])
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        def dfs(sr, sc):
            if sr < 0 or sr >= ROWS or sc < 0 or sc >= COLS or image[sr][sc] != orig_color:
                return
            image[sr][sc] = color
           
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)
            
        dfs(sr, sc)
        return image