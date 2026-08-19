class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(len(prices) - 1):
            if prices[i] < prices [i+1]:
                profit += prices[i+1] - prices[i]
        return profit

        # [4, 2, 3, 6, 2, 3] # expect 5
        #               ^ 
        # profit = 5