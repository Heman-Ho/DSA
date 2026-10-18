class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        res = [] 

        def backtrack(i, dots_remain):
            if dots_remain == 0: 
                if i >= len(s):
                    res.append(".".join(path))
                return
            
            for j in range(i, min(i+3, len(s))):
                segment = s[i:j+1]
                if (j > i and s[i] == "0") or int(segment) > 255:
                    break
                path.append(segment)
                backtrack(j+1, dots_remain - 1)
                path.pop()

        backtrack(0, 4)
        return res

        # 101023 
        # res = [] 
        # path = [1, 0, 1, 0] 
        # i = 0