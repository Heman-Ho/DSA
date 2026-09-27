class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        largest = 0
        # let dp[i][j] represent the largest square's side length with i, j as the upper left corner
        dp_upper = [0] * (COLS + 1)
        dp_lower = [0] * (COLS + 1)
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if matrix[i][j] == "1":
                    dp_upper[j] = 1 + min(dp_lower[j], dp_lower[j+1], dp_upper[j+1])
                    largest = max(largest, dp_upper[j])
            dp_lower = dp_upper
            dp_upper = [0] * (COLS + 1)
        
        return largest * largest