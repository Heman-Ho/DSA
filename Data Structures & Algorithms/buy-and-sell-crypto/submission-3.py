class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            else:
                res = max(res, price - buy_price)
        
        return res