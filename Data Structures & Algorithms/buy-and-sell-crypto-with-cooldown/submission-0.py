class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Define 3 states: Hold, Sell, Rest
        # let Hold[i] represent the max profit we would have if we are holding a stock on day i
        # Let Sell[i] represent the max profit we would have if we are selling a stock on day i
        # Let Rest[i] represent the max profit we would have if we do not have a stock and not buying or selling on day i
        hold = [0] * len(prices)
        sell = [0] * len(prices)
        rest = [0] * len(prices)

        # Define Base Cases
        hold[0] = -prices[0] # we bought a stock on day 1
        sell[0] = 0          # impossible to sell on day 1
        rest[0] = 0          # 0 profit if we don't buy 

        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            rest[i] = max(rest[i-1], sell[i-1])
        
        return max(sell[-1], rest[-1])