class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # let dp[i][j] represent the max number of points you can obtain from starting at points[i][j]
        ROWS = len(points)
        COLS = len(points[0])

        dp = [[0] * COLS for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c1 in range(COLS):
                for c2 in range(COLS):
                    dp[r][c1] = max(dp[r][c1], points[r][c1] + dp[r+1][c2] - abs(c1 - c2))
    
        return max(dp[0])