class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0

        for r in range(len(nums)):
            cur = max(nums[r], cur + nums[r])
            res = max(res, cur)
        
        return res