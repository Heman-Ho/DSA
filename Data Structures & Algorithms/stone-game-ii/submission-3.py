from functools import cache
from typing import List


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @cache
        def dfs(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix[i]

            min_opponent_stones = float("inf")
            for X in range(1, 2 * M + 1):
                min_opponent_stones = min(
                    min_opponent_stones, dfs(i + X, max(M, X))
                )

            return suffix[i] - min_opponent_stones

        return dfs(0, 1)