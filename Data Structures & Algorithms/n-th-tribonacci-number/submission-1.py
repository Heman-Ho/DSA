class Solution:
    def tribonacci(self, n: int) -> int:
        # Handle edge cases
        if n == 0:
            return 0
        if n <= 2:
            return 1

        prev3 = 0
        prev2 = 1
        prev1 = 1

        for i in range(3, n+1):
            Ti = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = Ti
        
        return Ti