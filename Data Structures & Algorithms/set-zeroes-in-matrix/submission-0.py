class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_zeros = [False] * ROWS
        col_zeros = [False] * COLS
        # Pass 1: mark r and c if it contains a 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_zeros[r] = True
                    col_zeros[c] = True
        
        # Pass 2: convert 1s to 0s if it's row or col is marked
        for r in range(ROWS):
            for c in range(COLS):
                if row_zeros[r] or col_zeros[c]:
                    matrix[r][c] = 0
