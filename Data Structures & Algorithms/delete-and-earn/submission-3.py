class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        points = [0] * (n + 1)
        for x in nums:
            points[x] += x

        # dp[v] = max points earnable considering values 0..v
        dp = [0] * (n + 1)
        dp[0] = points[0]
        dp[1] = max(points[0], points[1])

        for v in range(2, n + 1):
            dp[v] = max(dp[v - 1],
                        dp[v - 2] + points[v])

        return dp[n]