class Solution:
    def removeStars(self, s: str) -> str:   
        # ab*cd*ef -> acef
        stack = [] 

        for c in s:
            if c == "*":
                if stack:stack.pop()
            else:
                stack.append(c)
            
        return "".join(stack)
