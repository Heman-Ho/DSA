class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = x^(n//2) * x^((n + 1)//2)
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        

        half = self.myPow(x, n//2)
        return half * half * (x if n % 2 == 1 else 1)

        # what if x is negative? 
        # -3^3 = -3^1 * -3^2 works
        # -3^4 = -3^2 * -3^2 works

        # what if n is negative
