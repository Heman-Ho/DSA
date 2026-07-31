class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # The len of one side of the square is sum(matchsticks) / 4
        if sum(matchsticks) % 4 != 0:
            return False
        side_len = sum(matchsticks) // 4

        # We need to find subsets of matchsticks that sum up to side_len
        # Keep a set called used that tracks whether we used each matchstick in a subset
        used = set()

        matchsticks.sort(reverse=True)

        def backtrack(i, sides_remain, cur_side_len):
            if sides_remain == 0:
                return True
            if cur_side_len == side_len:
                return backtrack(0, sides_remain-1, 0)
            
            for j in range(i, len(matchsticks)):
                if j in used or cur_side_len + matchsticks[j] > side_len:
                    continue
                if j > i and matchsticks[j] == matchsticks[j-1] and (j-1) not in used:
                    continue

                used.add(j)
                if backtrack(j+1, sides_remain, cur_side_len + matchsticks[j]):
                    return True
                used.remove(j)
            return False
        
        return backtrack(0, 4, 0)

            
