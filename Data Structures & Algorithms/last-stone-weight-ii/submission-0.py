class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        # dp[w] stores whether a subset sum equal to 'w' is achievable
        dp = [False] * (target + 1)
        dp[0] = True  

        for stone in stones:
            # Iterate backward to avoid using the same stone twice
            for w in range(target, stone - 1, -1):
                if dp[w - stone]:
                    dp[w] = True

        # Find the largest reachable sum <= target
        for w in range(target, -1, -1):
            if dp[w]:
                best_s1 = w
                break

        # S1 - S2 = (total_sum - best_s1) - best_s1 = total_sum - 2 * best_s1
        return total_sum - 2 * best_s1