class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Let dp[i] represent the number of ways to make target i with nums
        # dp[i] = sum(dp[i-num]) for num in nums ( if i - num >= 0)
        # We are allowed to reuse each number => Use for num in nums in the nested loop

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums: 
                if i - num >= 0:
                    dp[i] += dp[i-num]        
        return dp[target]
