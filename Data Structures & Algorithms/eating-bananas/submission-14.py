import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 4 3 2 h=9
        l, r = 1, max(piles)

        while l < r:
            # converge this window to the optimal eating rate
            k = (l + r) // 2

            # simulate time taken to eat the piles with eating rate of k
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / k)
                if time_taken > h:
                    break

            if time_taken > h:
                # increase the eating rate
                l = k + 1
            # otherwise
            else:
                r = k
        
        return l
        
        # 25 10 23 4