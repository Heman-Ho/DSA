class Solution:
    def mySqrt(self, x: int) -> int:
        # The sqrt of any number x must be in the range [0, x]
        # Use a binary search on that range to find the sqrt
        l = 0
        r = x

        # if x = 10, res = 3

        while l < r:
            m = (l + r) // 2
            product = m * m
            if product == x:
                return m
            elif product > x:
                r = m - 1
            else:
                l = m + 1 
        
        if l * l > x:
            return l - 1
        else:
            return l