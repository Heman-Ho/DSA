class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [1 5 3 2 6 1] => return 5
        
        buy_price = float('inf')
        res = 0

        for price in prices:
            buy_price = min(buy_price, price)
            res = max(res, price - buy_price)
        
        return res