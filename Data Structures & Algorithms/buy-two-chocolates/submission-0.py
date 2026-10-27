class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        def get_least():
            least = prices[0]
            least_i = 0
            for i, price in enumerate(prices):
                if price < least:
                    least = price
                    least_i = i
            return (least, least_i)
        
        least, least_i = get_least()
        prices[least_i] = float('inf')
        second_least, _ = get_least()

        leftover = money - least - second_least
        return leftover if leftover >= 0 else money
            