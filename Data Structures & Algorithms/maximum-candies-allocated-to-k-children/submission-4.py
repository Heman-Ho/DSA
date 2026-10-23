class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, sum(candies) // k
        while l < r:
            m = (l + r + 1) // 2
            children = 0
            for pile in candies:
                children += pile // m
                if children >= k:
                    break
            if children >= k:
                l = m
            else:
                r = m - 1
        return l