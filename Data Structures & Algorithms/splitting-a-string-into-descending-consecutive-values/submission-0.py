class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(i, prev):
            if i == n:
                return True
            val = 0
            for j in range(i, n):
                val = val * 10 + int(s[j])
                if val > prev - 1:
                    break
                if val == prev - 1 and dfs(j + 1, val):
                    return True
            return False


        for i in range(n - 1):
            if dfs(i + 1, int(s[: i + 1])):
                return True
        return False