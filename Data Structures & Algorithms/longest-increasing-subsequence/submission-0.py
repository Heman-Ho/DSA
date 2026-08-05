class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let dp[i] hold the LIS using nums[i] as the last number of the LIS
        # dp[i] = max(dp[j]) + 1 for all 0 < j < i s.t. nums[i] > nums[j]
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)