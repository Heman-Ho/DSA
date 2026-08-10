class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # let greatest[i] represent the largest product you can get with the first i nums
        # greatest[i] = max(greatest[i-1], greatest[i-1] * nums[i], least[i-1] * nums[i])
        # let least[i] represent the smallest product you can get with the first i nums
        # least[i] = min(least[i-1], greatest[i-1] * nums[i], least[i-1] * nums[i])
        greatest = [nums[0]] * len(nums)
        least = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            greatest[i] = max(nums[i], greatest[i-1] * nums[i], least[i-1] * nums[i])
            least[i] = min(nums[i], greatest[i-1] * nums[i], least[i-1] * nums[i])
        
        return max(greatest)