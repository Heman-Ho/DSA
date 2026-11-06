class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # buy as many from the lowest end, sell from high end
        tokens.sort()
        cur_points = best_points = 0
        l, r = 0, len(tokens) - 1
        
        while l <= r:
            while l < len(tokens) and power >= tokens[l]:
                power -= tokens[l]
                cur_points += 1
                best_points = max(best_points, cur_points)
                l += 1

            if cur_points == 0:
                return 0
                
            cur_points -= 1
            power += tokens[r]
            r -= 1
        
        return best_points