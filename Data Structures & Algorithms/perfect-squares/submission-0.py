class Solution:
    def numSquares(self, n: int) -> int:
        # Let dp[i] represent the least number of perfect square numbers that sum to i
        # dp[i] = min(dp[i-perf_square] + 1for all 1 <= perfect squares <= i) 
        perf_squares = []
        for num in range(1, n+1):
            if num * num <= n:
                perf_squares.append(num * num)
            else:
                break
   

        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            for perf_square in perf_squares:
                if i - perf_square < 0:
                    break
                dp[i] = min(dp[i], dp[i-perf_square] + 1)
        
        return dp[n]

