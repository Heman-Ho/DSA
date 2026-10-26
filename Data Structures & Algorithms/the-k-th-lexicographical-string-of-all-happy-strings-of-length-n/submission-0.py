class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        num_happy = 0
        path = []
        
        # ab, ac, ba, bc, ca, cb

        def backtrack(i):
            nonlocal num_happy

            if i == n:
                num_happy += 1
                return
            
            for c in "abc":
                if not path or path[-1] != c:
                    path.append(c)
                    backtrack(i+1)
                    if num_happy == k:
                        return "".join(path)
                    path.pop()
        
        
        return backtrack(0) or ""
