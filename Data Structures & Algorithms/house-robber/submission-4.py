class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i] represent the max amount you can rob from the first i houses
        # dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # Only need to keep track of the max amount from the prev 2 houses -> O(1) space

        prev = 0
        prev2 = 0
        cur = 0

        for num in nums:
            cur = max(num + prev2, prev)
            prev2 = prev
            prev = cur
        
        return cur