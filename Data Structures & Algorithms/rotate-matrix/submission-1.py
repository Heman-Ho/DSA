class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1 2 3     7 4 1 
        # 4 5 6 ->  8 5 2 
        # 7 8 9     9 6 3

        ROWS, COLS = len(matrix), len(matrix[0]) 
        
        # Transpose then reverse each row
        # 1. Transpose
        for row in range(ROWS - 1):
            for col in range(row + 1, COLS):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        # 2. Reverse each row
        for row in matrix:
            row.reverse()
        
        