class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # keep a stack of open brackets
        stack = [] 
        for bracket in s:
            if bracket in ")]}":
                if (
                    not stack or 
                    mp[bracket] != stack.pop()
                ):
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0