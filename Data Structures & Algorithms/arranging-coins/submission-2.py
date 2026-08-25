class Solution:

    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            stair_size = (l + r) // 2
            coins_used = stair_size * (stair_size + 1) // 2

            if coins_used <= n:
                res = stair_size  # Valid row count found; try to find a larger one
                l = stair_size + 1
            else:
                r = stair_size - 1  # Too many coins used; look smaller

        return res