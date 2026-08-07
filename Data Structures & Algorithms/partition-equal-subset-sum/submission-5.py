class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        
        # let dp[i] represent whether there exists a subset that adds up to i
        dp = [False] * (target + 1)

        # Base Case
        dp[0] = True

        # We loop through nums because we don't want to reuse any number (subset)
        for num in nums:
            for amount in range(target, num-1, -1):
                if dp[amount - num]:
                    dp[amount] = True
              
        print(dp)
        return dp[target]