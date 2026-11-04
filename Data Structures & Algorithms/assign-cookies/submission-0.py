class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        
        i = 0
        # for each cookie, give it to the first child possible
        for cookie in s:
            if g[i] > cookie:
                continue
            i += 1
            
            if i == len(g):
                return i
        
        return i