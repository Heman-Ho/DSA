class Solution:
    def makeGood(self, s: str) -> str:
        # abBA
        
        stack = [] 
        for c in s:
            if stack and stack[-1] != c and (stack[-1] == c.upper() or stack[-1] == c.lower()):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)