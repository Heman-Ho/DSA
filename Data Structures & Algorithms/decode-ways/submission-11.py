class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        A = [0] * (len(s) + 1)
        A[0] = 1
        A[1] = 1

        for i in range(2, len(A)):
            if int(s[i-2:i]) <= 26 and s[i-2] != "0":
                A[i] += A[i-2]
            if s[i-1] != "0":
                A[i] += A[i-1]

        return A[-1]
