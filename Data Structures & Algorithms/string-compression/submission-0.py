class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        count = 0

        # a 3 a 
        for r in range(len(chars) + 1):        
            if r == len(chars) or (r != 0 and chars[r] != chars[r-1]):
                chars[l] = chars[r-1]
                l += 1
                if count > 1:
                    for c in str(count):
                        chars[l] = c
                        l += 1
                count = 1
            else:
                count += 1
        

        
        return l



            