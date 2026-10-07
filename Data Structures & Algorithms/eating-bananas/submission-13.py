import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1, 4, 3, 2 
        # h = 9
        # k = 2

        # possible answers for k is [1, max(piles)]
        l, r = 1, max(piles)

        # perform a binary search to find the lowest k
        while l < r:
            k = (l + r) // 2
            # for each k value checked, we need to simulate eating piles to see how many hours
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile / k)

            # if num hours > h: l = k + 1
            if num_hours > h:
                l = k + 1
            # otherwise r = k
            else:
                r = k
            
        return l