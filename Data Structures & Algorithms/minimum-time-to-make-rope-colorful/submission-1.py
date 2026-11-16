class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        run_max = 0
        for i, t in enumerate(neededTime):
            if i > 0 and colors[i] != colors[i-1]:
                run_max = 0
            res += min(t, run_max)
            run_max = max(run_max, t)
        return res