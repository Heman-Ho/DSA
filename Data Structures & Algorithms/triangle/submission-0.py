class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        row_len = ROWS

        dp = []
        for r in range(ROWS):
            dp.append([float('inf')] * (r+1))
        dp[0][0] = triangle[0][0]

        for r in range(1, ROWS):
            for c in range(r+1):
                if c-1 >= 0:
                    dp[r][c] = min(dp[r][c], triangle[r][c] + dp[r-1][c-1])
                if c < r:
                    dp[r][c] = min(dp[r][c], triangle[r][c] + dp[r-1][c])
     
        return min(dp[-1])
                    