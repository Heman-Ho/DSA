class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        # Can we make target out of a subset of nums? 
        # Let dp[i] hold whether or not we can make the value i out of nums
        # dp[i] = dp[i-num1] or dp[i-num2] or ...
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        
        return dp[-1]

        #   [1 2 3 4]
        # [T T T T ]