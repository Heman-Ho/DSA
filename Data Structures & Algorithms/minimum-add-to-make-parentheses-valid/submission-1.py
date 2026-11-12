class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Remove all matching parenthesis
        num_open = 0
        res = 0
        for c in s:
            if c == ")" and num_open > 0:
                num_open -= 1
            elif c == ")":
                res += 1
            else:
                num_open += 1

        return res + num_open
