class Solution:
    def minimumSteps(self, s: str) -> int:
        # keep track of insert position 
        # 1 1 0 1 
        #       ]i
        # j
        # res = 4
        res = 0
        i = len(s) - 1
   
        for j in range(len(s) - 1, -1, -1):
            if s[j] == "1":
                res += (i-j)
                i -= 1
            
        return res