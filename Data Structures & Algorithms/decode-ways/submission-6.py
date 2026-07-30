class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        prev2 = 1 
        prev1 = 1
        cur = 0

        for i in range(1, len(s)):
            # We can decode the digit before and the current digit together as a single letter
            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += prev2
            # We can decode the current digit as a single letter
            if s[i] != "0":
                cur += prev1
            
            prev2 = prev1
            prev1 = cur
            cur = 0

        return prev1
