class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l < r:
            m = (l+r) // 2
            print(m)
            time = 0
            for pile in piles:
                if time > h:
                    break
                time += (pile + m - 1) // m
                
            if time > h:
                l = m + 1
            else:
                r = m 
        
        return r