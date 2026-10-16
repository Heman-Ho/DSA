class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # for every cell, 
            # if the cell is 0, mark it's row and col with a -1 

            # 0 1 0     0 0 0
            # 1 1 1  -> 0 1 0
            # 1 1 1     0 1 0

            # - 1 -
            # 1 1 0 
            # 1 1 0 
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = -1
                    matrix[r][0] = -1
                    if r == 0:
                        first_row_zero = True
                    if c == 0:
                        first_col_zero = True
        
        for r in range(1, ROWS): 
            for c in range(1, COLS):
                if matrix[r][0] == -1 or matrix[0][c] == -1:
                    matrix[r][c] = 0

        # replace marked on first col
        for r in range(ROWS):
            if matrix[r][0] == -1 or first_col_zero:
                matrix[r][0] = 0

        # replace marked on first row
        for c in range(COLS):
            if matrix[0][c] == -1 or first_row_zero:
                matrix[0][c] = 0

        
