class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max, global_min = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0
        
        for num in nums:
            cur_max = max(cur_max + num, num)
            global_max = max(global_max, cur_max)
            
            cur_min = min(cur_min + num, num)
            global_min = min(global_min, cur_min)
            
            total += num
            
        # If all numbers are negative, global_max is the best we can do
        return global_max if global_max < 0 else max(global_max, total - global_min)