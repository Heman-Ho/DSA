class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces.append(len(s))
        
        l = 0
        for r in spaces:
            res.append(s[l:r])
            l = r
        
        return " ".join(res)