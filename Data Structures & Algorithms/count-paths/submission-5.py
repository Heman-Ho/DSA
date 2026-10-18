class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # let dp[i][j] represent number of unique paths to get to grid[i][j]
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # compact that into one row
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] += dp[j-1]

        # 0 1 3 6 10 15 21
        
        return dp[-1]