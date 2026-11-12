class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Remove all matching parenthesis
        stack = []
        res = 0
        for c in s:
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif c == ")":
                res += 1
            else:
                stack.append(c)

        # "(("
        # stack: "( ( ("
        # res = 3
        return res + len(stack)
