class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        
        # use a sliding window and a set to keep track of what's in the window
        l = 0 
        res = 0
        window_contents = set()

        for r in range(len(s)):
            while s[r] in window_contents:
                window_contents.remove(s[l])
                l += 1
            window_contents.add(s[r]) 
            res = max(res, r - l + 1)
        
        return res