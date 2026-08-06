class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            # Base case
            if len(path) == k:
                res.append(path.copy())

            for j in range(i, n + 1):
                path.append(j)
                backtrack(j+1)
                path.pop()
        backtrack(1)
        return res