class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Define 3 states: Hold, Sell, Rest
        # let Hold[i] represent the max profit we would have if we are holding a stock on day i
        # Let Sell[i] represent the max profit we would have if we are selling a stock on day i
        # Let Rest[i] represent the max profit we would have if we do not have a stock and not buying or selling on day i
        # since we only need to keep track of the values from the day before, we can save space by using scalars instead

        # Define Base Cases
        prev_hold = -prices[0]  # we bought a stock on day 1
        prev_sell = 0           # impossible to sell on day 1
        prev_rest = 0           # 0 profit if we don't buy 

        for i in range(1, len(prices)):
            hold = max(prev_hold, prev_rest - prices[i])
            sell = prev_hold + prices[i]
            rest = max(prev_rest, prev_sell)

            prev_hold = hold
            prev_sell = sell
            prev_rest = rest
        
        return max(prev_sell, prev_rest)