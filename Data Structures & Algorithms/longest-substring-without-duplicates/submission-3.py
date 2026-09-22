from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        counts = defaultdict(int)
        res = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
            

                
