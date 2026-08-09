class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        seen = set()

        for letter in s:
            if letter in seen:
                continue
            seen.add(letter)

            num_replacements = k
            l, r = 0, 0
            while r < len(s):
                if s[r] == letter:
                    r += 1
                elif num_replacements > 0:
                    num_replacements -= 1
                    r += 1
                else:
                    if s[l] != letter:
                        num_replacements += 1
                    l += 1
                ret = max(ret, r - l)
                
        
        return ret