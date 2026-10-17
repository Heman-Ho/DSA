class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # let dp[i][j] represent the min sum to reach  grid[i][j] 
        # dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # we only need to keep track of one row
        dp = [float('inf')] * (len(grid[0]) + 1)
        dp[1] = 0

        for i in range(len(grid)):
            for j in range(1, len(grid[0]) + 1):
                dp[j] = grid[i][j-1] + min(dp[j], dp[j-1])
        

        # 1 2 0
        # 5 4 2
        # 1 1 3

        # 0, inf, inf, inf
        return dp[-1]
