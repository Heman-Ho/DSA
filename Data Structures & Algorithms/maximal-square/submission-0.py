class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        largest = 0
        # let dp[i][j] represent the largest square's side length with i, j as the upper left corner
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    largest = max(largest, dp[i][j])
        
        return largest * largest