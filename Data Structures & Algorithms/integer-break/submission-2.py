class Solution:
    def integerBreak(self, n: int) -> int:
        # Let dp[i] hold the maximum product you can get with input i
        # dp[i] = max(dp[i-j] * j for j in range(1, i))
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j] * j, j * (i-j))

        return dp[n]