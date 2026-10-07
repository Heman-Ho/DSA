class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # let dp[i] represent the fewest number of coins it takes to make target i
        # dp[i] = min(dp[i-coin] for coin in coins)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i-coin])
            # print(f"coin {coin} introduced, dp array: {dp}")
            
        return -1 if dp[amount] == float('inf') else dp[amount]