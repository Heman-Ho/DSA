class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            # Base case
            if len(path) == k:
                res.append(path.copy())
                return

            for j in range(i, n + 1):
                # Prune if there are not enough remaining numbers to fill the path
                if n - j + 1 < k - len(path):
                    break
                path.append(j)
                backtrack(j+1)
                path.pop()
        backtrack(1)
        return res