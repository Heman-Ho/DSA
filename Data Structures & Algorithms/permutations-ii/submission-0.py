from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        choices = Counter(nums)

        def backtrack():
            if len(path) ==  len(nums):
                res.append(path.copy())
                return
            for choice, amount in choices.items():
                if amount == 0:
                    continue
                path.append(choice)
                choices[choice] -= 1
                backtrack()
                choices[choice] += 1
                path.pop()

        backtrack()
        return res
