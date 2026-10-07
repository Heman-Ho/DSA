class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 101023
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        path = []


        # 101023
        # 
        # brute force using a backtracking technique to inject 4 dots 
        def backtrack(i, dots):
            if dots == 4 and i >= len(s):
                res.append(".".join(path))
                return
            
            for j in range(i, min(len(s), i + 3)):
                # if it's a leading 0 or > 255, then don't explore that path
                if (s[i] == "0" and j > i) or int(s[i:j+1]) > 255:
                    break
                path.append(s[i:j+1])
                backtrack(j+1, dots + 1)
                path.pop()
        
        backtrack(0, 0)
        return res
            