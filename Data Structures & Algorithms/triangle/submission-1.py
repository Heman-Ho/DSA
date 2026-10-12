class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
   
        prev_row = [triangle[0][0]] * ROWS
        new_row = [float('inf')] * ROWS

        for r in range(1, ROWS):
            for c in range(r+1):
                if c-1 >= 0:
                    new_row[c] = min(new_row[c], triangle[r][c] + prev_row[c-1])
                if c < r:
                    new_row[c] = min(new_row[c], triangle[r][c] + prev_row[c])
            prev_row = new_row
            new_row = [float('inf')] * ROWS
            
     
        return min(prev_row)
                    