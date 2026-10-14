class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > min_price:
                res = max(res, prices[i] - min_price)
            else:
                min_price = prices[i]
        
        return res