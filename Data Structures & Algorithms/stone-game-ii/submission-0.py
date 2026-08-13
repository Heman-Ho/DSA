class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        prefix_sums = [0] * (len(piles) + 1)
        for i in range(1, len(piles) + 1):
            prefix_sums[i] = prefix_sums[i-1] + piles[i-1]


        def dfs(i, is_alice, m):
            if i >= len(piles):
                return 0
            if (i, is_alice, m) in cache:
                return cache[(i, is_alice, m)]
            
            
            if is_alice:
                res = 0
                for j in range(i, i + 2*m):
                    if j >= len(piles):
                        break
                    sum_piles = prefix_sums[j+1] - prefix_sums[i]
                    res = max(res, sum_piles + dfs(j+1, False, max(m, j-i+1)))
            else:
                res = float('inf')
                for j in range(i, i + 2*m):
                    if j >= len(piles):
                        break
                    res = min(res, dfs(j+1, True, max(m, j-i+1)))
            cache[(i, is_alice, m)] = res

            return res
        
        return dfs(0, True, 1)