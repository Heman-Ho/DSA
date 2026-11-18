class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 5 1 0 2 3 4 5 
        res = 0
        cur = 0

        for i, num in enumerate(nums):
            if i == 0 or num > nums[i-1]:
                cur += num
            else:
                cur = num
            res = max(res, cur)
        
        return res