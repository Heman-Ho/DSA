from functools import cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def solve(text):
            result = []
            for i, op in enumerate(text):
                if op in '+-*':
                    for a in solve(text[:i]):
                        for b in solve(text[i+1:]):
                            result.append(a+b if op=='+' else a-b if op=='-' else a*b)
            if not result: 
                result.append(int(text))
            return result

        return solve(expression)
