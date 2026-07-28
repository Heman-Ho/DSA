class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
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

