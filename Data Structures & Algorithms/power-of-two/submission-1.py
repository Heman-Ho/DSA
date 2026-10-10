class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
            
        bin_rep = bin(n)

        for c in bin_rep[3:]:
            if c == "1":
                return False
        
        return True