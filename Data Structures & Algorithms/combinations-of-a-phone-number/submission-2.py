class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        combination = []

        # handle edge case
        if len(digits) == 0:
            return []

        # Keep track of index i representing the digit index
        def backtrack(i):
            if len(combination) == len(digits):
                res.append("".join(combination))
                return
            
            for c in mapping[digits[i]]:
                combination.append(c)
                backtrack(i+1)
                combination.pop()

        backtrack(0)
        return res

