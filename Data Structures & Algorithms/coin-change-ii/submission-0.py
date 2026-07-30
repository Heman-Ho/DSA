class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Let dp[i,j] = the number of distinct combinations using the first i coins
        # that total up to amount j

        # Return dp[len(coins), amount]
        # dp[i,j] = sum(dp[i-1, amount - n*coins[i]] for every n such that n*coins[i] is <= amount)

        # dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # for i in range(1, len(coins)+1):
        #     for j in range(1, amount+1):
        #         sum = 0
        #         for n in range()

        A = [0] * (amount + 1)
        A[0] = 1

        for coin in coins:
            for i in range(len(A)):
                if i - coin >= 0:
                    A[i] += A[i-coin]
        print(A)
        return A[-1]
                
        
        # (1,1,1), (2,1), (3)
        # (1,2)
