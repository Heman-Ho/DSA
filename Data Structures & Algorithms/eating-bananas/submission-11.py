import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # range of possible answers for k: 1 - max(piles)
        # binary search in O(log n)
        l, r = 1, max(piles)

        while l < r:
            # check how many hours it takes with eating rate of k: O(n)
            m = (l + r) // 2
            num_hours = 0

            for pile in piles:
                num_hours += math.ceil(pile / m)
            
            if num_hours > h: # we need a larger eating rate
                l = m + 1
            else: # we can try a smaller eating rate
                r = m
        
        return l
