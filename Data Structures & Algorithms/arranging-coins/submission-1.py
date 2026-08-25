class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair_size = 1
        coins_used = 0

        while coins_used + stair_size <= n:
            coins_used += stair_size
            stair_size += 1

        return stair_size - 1