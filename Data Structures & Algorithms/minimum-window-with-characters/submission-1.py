from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        desired = Counter(t)
        counts = defaultdict(int)

        def isValid(): # (O(1) because len(counts) <= 48) 
            for c, desired_cnt in desired.items():
                if counts[c] < desired_cnt:
                    return False
            return True

        res = ""
        l = 0
        r = 0
        while r < len(s):
            while not isValid() and r < len(s):
                counts[s[r]] += 1
                r += 1
            if not isValid():
                return res
            while isValid():
                counts[s[l]] -= 1
                l += 1
            if res == ""  or len(res) > r - l:
                res = s[l-1:r]
            
        return res
                
