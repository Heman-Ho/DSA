from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
       
        @cache
        def dfs(l: int, r: int) -> int:
            if l == r:
                return piles[l]
            return max(piles[l] - dfs(l + 1, r), piles[r] - dfs(l, r - 1))


        return dfs(0, len(piles) - 1) > 0