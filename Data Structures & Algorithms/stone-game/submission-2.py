class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        
        def play(l: int, r: int, alice_turn: bool) -> int:
            if (l, r, alice_turn) in cache:
                return cache[(l, r, alice_turn)]
            if l > r:
                return 0
            if l == r:
                return piles[l] if alice_turn else 0

            if alice_turn:
                res = max(piles[l] + play(l+1, r, False), piles[r] + play(l, r-1, False))
            else:
                res = min(play(l+1, r, True), play(l, r-1, True))
            
            cache[(l, r, alice_turn)] = res
            return res

        return play(0, len(piles) - 1, True) > sum(piles) // 2