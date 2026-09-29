class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def dfs(i: int, M: int, alice_turn: bool) -> int:
            if i >= len(piles):
                return 0
            if (i, M, alice_turn) in cache:
                return cache[(i, M, alice_turn)]
            if i + 2 * M >= len(piles):
                return sum(piles[i:]) if alice_turn else 0

            if alice_turn:
                res = 0
                pile_size = 0
                for X in range(1, 2*M + 1):
                    pile_size += piles[i+X-1]
                    res = max(res, pile_size + dfs(i+X, max(M, X), False))
            else:
                res = float('inf')
                for X in range(1, 2*M + 1):
                    res = min(res, dfs(i+X, max(M, X), True))
                
            cache[(i, M, alice_turn)] = res
            return res

        return dfs(0, 1, True)
